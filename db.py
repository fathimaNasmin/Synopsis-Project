from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Create a table name "student"
class Students(db.Model):
    """student table class"""
    __tablename__ = 'students'
    enroll_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)#date datatype
    contact_num = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    course = db.Column(db.String(10), nullable=False)


    def __init__(self, username, email):
        self.username = username
        self.email = email