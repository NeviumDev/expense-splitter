from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expenses = db.relationship("Expense", backref="payer", lazy=True)


class Expense(db.Model):
    __tablename__ = "expense"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)
