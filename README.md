<h1>📸 AttendEase – AI Powered Attendance System</h1>

<p>
AttendEase is a Flask-based smart attendance system that uses <b>Face Recognition + Machine Learning</b>
to automatically mark student attendance and notify parents via email when a student is absent.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>AI Face Recognition Attendance</li>
  <li>Manual Attendance Backup</li>
  <li>Student Management (Add / Delete)</li>
  <li>Parent Email Notification for Absentees</li>
  <li>Dashboard with Present / Absent Count</li>
  <li>Real-time Face Detection using OpenCV</li>
  <li>CSV Attendance Reports</li>
  <li>KNN Machine Learning Model</li>
  <li>Gmail SMTP Integration</li>
</ul>

<hr>

<h2>🧠 How It Works</h2>

<h3>1️⃣ Student Registration</h3>
<p>
Teacher adds student name and parent email. System captures multiple face samples and stores them in pickle files.
</p>

<h3>2️⃣ Model Training</h3>
<p>
KNN model trains automatically using stored face data.
</p>

<h3>3️⃣ AI Attendance</h3>
<ul>
  <li>Teacher uploads classroom photo</li>
  <li>Faces detected using OpenCV</li>
  <li>Faces recognized using KNN</li>
  <li>Each student marked Present / Absent</li>
  <li>Duplicate faces ignored automatically</li>
  <li>Attendance saved into CSV file</li>
</ul>

<h3>4️⃣ Email Alerts</h3>
<p>
If student is absent, parent receives Gmail notification:<br>
<b>Your student &lt;name&gt; is absent on &lt;date&gt;</b><br>
Missing emails are safely skipped.
</p>

<h3>5️⃣ Dashboard</h3>
<ul>
  <li>Total Students</li>
  <li>Present</li>
  <li>Absent</li>
  <li>Attendance Status</li>
</ul>

<h3>6️⃣ Manual Attendance</h3>
<p>Fallback option for manual marking.</p>

<hr>

<h2>🛠 Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>OpenCV</li>
  <li>Scikit-Learn (KNN)</li>
  <li>Pandas</li>
  <li>SMTP (Gmail)</li>
  <li>HTML / CSS</li>
</ul>

<hr>

<h2>🗃️ Project Structure</h2>

<pre>
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
</pre>

<hr>

<h2>▶️ Run Locally</h2>

<pre>
pip install -r requirements.txt
python app.py
</pre>

<p>Open browser:</p>

<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2>🔐 Environment Variables (.env)</h2>

<pre>
EMAIL=yourgmail@gmail.com
PASSWORD=your_app_password
</pre>

<hr>

<h2>⚠️ Notes</h2>
<ul>
  <li>Camera runs locally</li>
  <li>Pickle files store trained faces</li>
  <li>Gmail App Password required</li>
  <li>GitHub contains only source code (not trained data)</li>
</ul>

<hr>

<h2>📌 Deployment</h2>
<p>
Free demo deployment using ngrok (local server exposed online).<br>
Cloud deployment requires paid GPU services.
</p>

<hr>

<img width="100%" src="https://github.com/user-attachments/assets/f41f9edb-464b-43fd-83bf-c10c130a12d7">
<br><br>
<img width="100%" src="https://github.com/user-attachments/assets/e4280f4f-3e03-4968-a3bc-50669cefd69f">
<br><br>
<img width="100%" src="https://github.com/user-attachments/assets/7334ca06-b803-4bcb-a2ed-03853501df41">
<br><br>
<img width="100%" src="https://github.com/user-attachments/assets/c3fdb97e-14e1-46ef-bf40-82e792ef2473">

<hr>

<h2>👩‍💻 Author</h2>
<p>☕ Sakshi Kumari</p>
