from datetime import datetime
from SEO import db, app
from flask_sqlalchemy import SQLAlchemy


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100))
    service = db.Column(db.String(100))
    star = db.Column(db.Integer)
    comments = db.Column(db.text())

    def __repr__(self, customer, email, service, star, comments):
        self.customer = customer
        self.email = email
        self.service = service
        self.star = star
        self.comments = comments



