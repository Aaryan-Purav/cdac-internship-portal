from flask import Blueprint, render_template, request, redirect, url_for, session
from . import db
from .models import Internship

main = Blueprint('main', __name__)
@main.route('/')
def home():
    internships = Internship.query.all()
    return render_template('home.html', internships=internships)

@main.route('/add', methods=['GET', 'POST'])
def add_internship():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        domain = request.form['domain']

        new_i = Internship(title=title, description=description, domain=domain)
        db.session.add(new_i)
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template('add.html')

