from flask_restful import Resource
from flask import request
from ..models import Internship, db

class InternshipList(Resource):
    def get(self):
        internships = Internship.query.all()
        return [{'id': i.id, 'title': i.title, 'domain': i.domain} for i in internships]

    def post(self):
        data = request.get_json()
        new_intern = Internship(
            title=data['title'],
            description=data['description'],
            domain=data['domain']
        )
        db.session.add(new_intern)
        db.session.commit()
        return {'message': 'Internship created successfully'}
