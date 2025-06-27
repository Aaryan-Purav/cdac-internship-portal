# Internship/Project Finder Portal

This is a Flask-based web application built as part of the 4-credit CDAC Transfer Project.

## 📌 Features

- Add and view VLSI/Tech internships
- REST API using Flask-RESTful
- Object-Oriented Programming and SQLAlchemy
- SQLite database integration
- Templating with Jinja2 (`home.html` and `add.html`)

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
```

Run the app:
```
python run.py
```

Then open in your browser:

Homepage: http://127.0.0.1:5000

Add Internship: http://127.0.0.1:5000/add

🔁 API Endpoints
GET /api/internships → Fetch all internships

POST /api/internships → Add internship using JSON

🧑‍💻 Sample JSON for POST:
{
  "title": "Analog Design Intern",
  "domain": "VLSI",
  "description": "Work with Spice simulation tools."
}

🙋 Built By
Aaryan
B.Tech. Electronics & Telecommunication
CDAC Transfer Project – June 2025

✅ Optional Enhancements
Add login/signup feature

Connect to a live PostgreSQL DB

Deploy on Render/Heroku

Add image uploads or resume attachment field


---

## 🛠 What to Do Next:

### 1. Replace your current `README.md` with the above content  
### 2. Save the file  
### 3. Stage and commit the fix:

```bash
git add README.md
git commit -m "Cleaned and finalized README.md"
git push
```
