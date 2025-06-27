# Internship/Project Finder Portal

This is a Flask-based web application built as part of the 4-credit CDAC Transfer Project.

## 📌 Features

- Add and view VLSI/Tech internships
- REST API using Flask-RESTful
- Object-Oriented Programming and SQLAlchemy
- SQLite database integration
- Templating with Jinja2 (home.html and add.html)

## 📂 Project Structure

Project/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ └── api/internships.py
├── templates/
│ ├── home.html
│ └── add.html
├── config.py
├── internships.db
├── run.py
├── requirements.txt
├── README.md


## ▶️ How to Run

1. Clone or unzip the project
2. Create a virtual environment (optional)
3. Install dependencies:

```bash
pip install -r requirements.txt

Run the app:
python run.py

Visit in browser:

Homepage: http://127.0.0.1:5000/

Add Internship: http://127.0.0.1:5000/add

🔁 API Endpoints
GET /api/internships → Fetch all internships

POST /api/internships → Add internship using JSON

🧑‍💻 Sample JSON for API
{
  "title": "Analog Design Intern",
  "domain": "VLSI",
  "description": "Work with Spice simulation tools."
}

🙋 Built By
Aaryan
B.Tech. Electronics & Telecommunication
CDAC Transfer Project – June 2025

---

### ✅ Step 4: Save the file

Once you've pasted the content:
- Hit **Ctrl + S** to save
- Done 🎯

---

## 🧠 Bonus Tip: Preview Markdown (Optional)

In **VS Code**:
- Right click on the file → `Open Preview`
- OR use shortcut: `Ctrl + K V`

This shows how your Markdown will look in GitHub or any other Markdown viewer.

---

Want a **fancy version** with badges, images, or custom table of contents? I can help with that too.

Let me know once you’ve created the README — we’ll zip it all up and call it done ✅🧳
