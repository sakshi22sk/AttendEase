from flask import Flask, render_template, redirect, request
import os, subprocess, pickle, csv, cv2, sys, sqlite3
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASS = os.getenv("GMAIL_PASS")

app = Flask(__name__)

DB = "database.db"

# ================= DATABASE =================

def get_db():
    return sqlite3.connect(DB)

def init_db():
    con = get_db()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        email TEXT
    )
    """)
    con.commit()
    con.close()

init_db()

# ================= EMAIL =================

def send_absent_mail(to_email, student):

    if not to_email:
        return

    try:
        msg = EmailMessage()
        msg["Subject"] = "Attendance Alert"
        msg["From"] = GMAIL_USER
        msg["To"] = to_email

        msg.set_content(
            f"Your student {student} is absent on {datetime.now().strftime('%A, %d %B %Y')}."
        )

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(GMAIL_USER,GMAIL_PASS)
            smtp.send_message(msg)

    except Exception as e:
        print("Email failed:", e)

# ================= TRAIN =================

def train():
    global knn, students

    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT name FROM students")
    students = [r[0] for r in cur.fetchall()]
    con.close()

    if not os.path.exists("data/names.pkl"):
        knn=None
        return

    labels=pickle.load(open("data/names.pkl","rb"))
    faces=pickle.load(open("data/faces_data.pkl","rb"))

    if len(labels)==0:
        knn=None
        return

    knn=KNeighborsClassifier(n_neighbors=5)
    knn.fit(faces,labels)

train()

# ================= DASHBOARD =================

@app.route("/")
def dashboard():

    done="Not Done"
    present=0
    absent=0
    total=0

    if os.path.exists("data/names.pkl"):
        labels=pickle.load(open("data/names.pkl","rb"))
        total=len(set(labels))

    if os.path.exists("Attendance") and os.listdir("Attendance"):
        latest=sorted(os.listdir("Attendance"))[-1]
        df=np.genfromtxt("Attendance/"+latest,delimiter=",",dtype=str,skip_header=1)

        done="Done"
        if df.size>0:
            present=len([x for x in df if x[1]=="Present"])
            absent=total-present

    return render_template("dashboard.html",
        done=done,
        total=total,
        present=present,
        absent=absent,
        now=datetime.now().strftime("%A, %d %B %Y")
    )

# ================= STUDENTS =================

@app.route("/students")
def manage():
    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT name FROM students")
    students=[r[0] for r in cur.fetchall()]
    con.close()
    return render_template("students.html",students=students)

@app.route("/add",methods=["POST"])
def add_student():

    name=request.form["name"]
    email=request.form.get("email","")

    con=get_db()
    cur=con.cursor()
    cur.execute("INSERT OR IGNORE INTO students(name,email) VALUES(?,?)",(name,email))
    con.commit()
    con.close()

    subprocess.call([sys.executable,"add_face.py",name])
    train()

    return redirect("/students")

@app.route("/delete/<name>")
def delete(name):

    con=get_db()
    cur=con.cursor()
    cur.execute("DELETE FROM students WHERE name=?",(name,))
    con.commit()
    con.close()

    train()
    return redirect("/students")

# ================= AI ATTENDANCE =================

@app.route("/take")
def take():

    if knn is None:
        return redirect("/")

    video=cv2.VideoCapture(0)
    facedetect=cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

    attendance=set()

    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT name,email FROM students")
    rows=cur.fetchall()
    con.close()

    while True:

        ret,frame=video.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=facedetect.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:

            crop=frame[y:y+h,x:x+w]
            resized=cv2.resize(crop,(50,50)).flatten().reshape(1,-1)

            name=knn.predict(resized)[0]
            dist=np.mean(knn.kneighbors(resized)[0])

            status="Already Marked"

            if dist<3500 and name not in attendance:
                attendance.add(name)
                status="Marked Present"

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,f"{name} - {status}",(x,y-10),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

        cv2.imshow("T = Capture | Q = Finish",frame)

        k=cv2.waitKey(1)

        if k==ord('q'):
            break

    if not os.path.exists("Attendance"):
        os.makedirs("Attendance")

    filename=f"Attendance/Attendance_{datetime.now().strftime('%H-%M-%S')}.csv"

    with open(filename,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["NAME","STATUS"])

        for name,email in rows:

            status="Present" if name in attendance else "Absent"
            writer.writerow([name,status])

            if status=="Absent":
                send_absent_mail(email,name)

    video.release()
    cv2.destroyAllWindows()

    return redirect("/")

# ================= MANUAL =================

@app.route("/manual",methods=["GET","POST"])
def manual():

    con=get_db()
    cur=con.cursor()
    cur.execute("SELECT name,email FROM students")
    rows=cur.fetchall()
    con.close()

    if request.method=="POST":

        present=request.form.getlist("present") or []

        filename=f"Attendance/Attendance_{datetime.now().strftime('%H-%M-%S')}.csv"

        with open(filename,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["NAME","STATUS"])

            for name,email in rows:

                status="Present" if name in present else "Absent"
                writer.writerow([name,status])

                if status=="Absent":
                    send_absent_mail(email,name)

        return redirect("/")

    return render_template("manual.html",students=[r[0] for r in rows])

# =================

if __name__=="__main__":
    app.run(debug=True)
