from flask import Flask, render_template, redirect
from data import db_session
import datetime
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    print("igushufghbdusfhogubd")
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    return render_template("index.html", jobs=jobs, users=users)


def add_user(name, surname, age, position, speciality, address, email):
    db_sess = db_session.create_session()
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    db_sess.add(user)
    db_sess.commit()
def add_work(team_leader, jobe, work_size, collaborators, is_finished):
    db_sess = db_session.create_session()
    job = Jobs()
    job.team_leader = team_leader
    job.job = jobe
    job.work_size = work_size
    job.collaborators = collaborators
    job.is_finished = is_finished
    db_sess.add(job)
    db_sess.commit()


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
