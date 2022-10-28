from flask import Flask, render_template, url_for, redirect, request
from forms import StudentLogin, Synopsis, EvaluatorLogin, AdminLogin
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = "abFvchh&89%gsdjsn"


@app.route('/', methods=['GET', 'POST'])
def student():
    curr_year = date.today().year
    student_login = StudentLogin()
    if student_login.validate_on_submit():
        synopsis_form = Synopsis()
        return render_template("studentlogin.html", form=synopsis_form)

    return render_template('index.html', year=curr_year, form=student_login)


# @app.route('/studentlogin', methods=['GET'])
# def student_login():



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
    app.run(debug=True)

