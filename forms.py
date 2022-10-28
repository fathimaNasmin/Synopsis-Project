from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FileField, SubmitField, PasswordField
from wtforms.validators import Length, InputRequired, DataRequired


class StudentLogin(FlaskForm):
    course = SelectField('Select Course', choices=[('', 'Select'), ('bca', 'BCA'), ('mca', 'MCA'), ('pgdca', 'PGDCA'), ('bsc', 'BSc')], validators=[InputRequired(message="Select the Course")])
    enrol_id = StringField('Enrollment Id', validators=[InputRequired(message="Enter the Enrollment id")])


class Synopsis(FlaskForm):
    project_category = SelectField('Project Category', choices=[('gui','GUI'), ('network','Networking'), ('web','Web Developement')], validators=[InputRequired()])
    title = StringField('Title', validators=[InputRequired()])
    guide_name = StringField('name', validators=[InputRequired()])
    guide_qualification = SelectField('qualification', choices=[('phd','PhD'), ('mtech','MTech'), ('btech','BTech'), ('mca','MCA'), ('msc','MSc')], validators=[InputRequired()])
    guide_experience = IntegerField('experience', validators=[InputRequired()])
    docs = FileField('docs', validators=[InputRequired()])
    submit = SubmitField('Submit')


class EvaluatorLogin(FlaskForm):
    login_id = StringField('id', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField('Submit')


class AdminLogin(FlaskForm):
    admin_id = StringField('admin_id', validators=[DataRequired()])
    admin_password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Submit')



