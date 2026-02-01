📸 **AttendEase** – AI Powered Attendance System

AttendEase is a Flask-based smart attendance system that uses Face Recognition + Machine Learning to automatically mark student attendance and notify parents via email when a student is absent.
🚀 Features-
AI Face Recognition Attendance
Manual Attendance Backup
Student Management (Add / Delete)
Parent Email Notification for Absentees
Dashboard with Present / Absent Count
Real-time Face Detection using OpenCV
CSV Attendance Reports
KNN Machine Learning Model
Gmail SMTP Integration

🧠 How It Works
1️⃣ Student Registration
Teacher adds student name + parent email.
System captures multiple face samples and stores them in pickle files.
2️⃣ Model Training
KNN model trains automatically using stored face data.
3️⃣ AI Attendance
Teacher uploads class student photo:
Faces detected using OpenCV
Faces recognized using KNN
Each student marked Present / Absent
Duplicate faces ignored automaticall
Attendance saved into CSV file.
4️⃣ Email Alerts
If student is Absent:
Parent receives Gmail notification:
Your student <name> is absent on <date>
Missing emails are safely skipped.
5️⃣ Dashboard
Latest attendance is displayed:
Total Students
Present
Absent
Attendance Status
6️⃣ Manual Attendance
Fallback option for manual marking.
🛠 Tech Stack
Python
Flask
OpenCV
Scikit-Learn (KNN)
Pandas
SMTP (Gmail)
HTML / CSS

🗃️Project Structure 
AttendEase/
│
├── app.py
├── add_face.py
├── students.csv
├── Attendance/
├── data/
│   └── haarcascade_frontalface_default.xml
├── templates/
├── static/
├── requirements.txt
├── .env
└── README.md

▶️ Run Locally
pip install -r requirements.txt
python app.py
Open browser:
http://127.0.0.1:5000

🔐 Environment Variables (.env)
EMAIL=yourgmail@gmail.com
PASSWORD=your_app_password

⚠️ Notes
Camera runs locally
Pickle files store trained faces
Gmail App Password required
GitHub contains only source code (not trained data)
📌 Deployment
Free demo deployment using ngrok (local server exposed online).
Cloud deployment requires paid GPU services.

<img width="1920" height="1080" alt="Screenshot (205)" src="https://github.com/user-attachments/assets/f41f9edb-464b-43fd-83bf-c10c130a12d7" />
<img width="1920" height="1080" alt="Screenshot (206)" src="https://github.com/user-attachments/assets/e4280f4f-3e03-4968-a3bc-50669cefd69f" />
<img width="1865" height="927" alt="Screenshot 2026-02-01 173417" src="https://github.com/user-attachments/assets/7334ca06-b803-4bcb-a2ed-03853501df41" />
<img width="1827" height="922" alt="Screenshot 2026-02-01 173547" src="https://github.com/user-attachments/assets/c3fdb97e-14e1-46ef-bf40-82e792ef2473" />

Author ☕
~ Sakshi kumari .
