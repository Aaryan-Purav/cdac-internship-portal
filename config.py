import os  # ✅ You need this import!

# ✅ Define this outside the class
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'internships.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
