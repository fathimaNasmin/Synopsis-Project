from flask import Flask, render_template, url_for, redirect, request, flash
from forms import StudentLogin, Synopsis, EvaluatorLogin, AdminLogin
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import _psycopg
from db import Students


app = Flask(__name__)
app.config['SECRET_KEY'] = "abFvchh&89%gsdjsn"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:amy0711@localhost/myDB'

db = SQLAlchemy(app)

db.init_app(app)
with app.app_context():
    db.create_all()


#routing
@app.route('/', methods=['GET', 'POST'])
def student():
    curr_year = date.today().year
    student_login = StudentLogin()
    if student_login.validate_on_submit():
        course = request.form['course'].upper()
        enrol_id = int(request.form['enrol_id'])
        dob = request.form['dob']
        user_object = db.session.query(Students).filter_by(enroll_id=enrol_id).first()
        if user_object is None:
            flash("Invalid Enrollment Id", "Info")
            return redirect(url_for('student'))
        elif not (user_object.enroll_id == enrol_id and user_object.course == course and
                  user_object.dob.strftime("%Y-%m-%d") == dob):
            flash("Student not exists", "Info")
            return redirect(url_for('student'))
        else:
            synopsis_form = Synopsis()
            return render_template("studentlogin.html", form=synopsis_form, user=user_object)

    return render_template('index.html', year=curr_year, form=student_login)


@app.route('/studentlogin/synopsis', methods=['GET', 'POST'])
def student_synopsis():
    return render_template()
    # return redirect(url_for("student_login")+"#synopsis-section")


@app.route('/studentlogin/message')
def std_message():
    return redirect(url_for("student_login")+"#message-section")



@app.route('/evaluator', methods=['GET', 'POST'])
def evaluator():
    evaluator_form = EvaluatorLogin()
    if evaluator_form.validate_on_submit():
        return render_template('evaluatorpage.html')
    return render_template('evaluator.html', form=evaluator_form)


@app.route('/evaluatorview')
def evaluator_view():
    return render_template('evaluatorviewpage.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    admin_form = AdminLogin()
    if admin_form.validate_on_submit():
        return render_template('adminview.html')
    return render_template('admin.html', form=admin_form)






if __name__ == '__main__':
    app.app_context().push()
    app.run(debug=True)

