from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FileField, SubmitField, PasswordField
from wtforms.validators import DataRequired,Length


class StudentLogin(FlaskForm):
    course = SelectField('Select Course', choices=[('', 'Select'), ('bca', 'BCA'), ('mca', 'MCA'), ('pgdca', 'PGDCA'), ('bsc', 'BSc')])
    enrol_id = StringField('Enrollment Id', validators=[DataRequired(), Length(min=7)])


class Synopsis(FlaskForm):
    project_category = SelectField('Project Category', choices=[('gui','GUI'), ('network','Networking'), ('web','Web Developement')])
    title = StringField('Title', validators=[DataRequired()])
    guide_name = StringField('name', validators=[DataRequired()])
    guide_qualification = SelectField('qualification', choices=[('phd','PhD'), ('mtech','MTech'), ('btech','BTech'), ('mca','MCA'), ('msc','MSc')])
    guide_experience = IntegerField('experience', validators=[DataRequired()])
    docs = FileField('docs', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EvaluatorLogin(FlaskForm):
    login_id = StringField('id', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField('Submit')


class AdminLogin(FlaskForm):
    admin_id = StringField('admin_id', validators=[DataRequired()])
    admin_password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Submit')



