from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vorota.db'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), default='Аноним')
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Сообщение от: {self.name}'


@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/info', methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        number = request.form['number']
        name = request.form['name']
        text = request.form['text']

        data = Message(number=number, name=name, text=text)

        try:
            db.session.add(data)
            db.session.commit()
            return redirect('/')
        except:
            return 'Произошла ошибка попробуйте ещё раз'
    else:
        return render_template('about.html', title='О Нас')


@app.route('/vorota')
def vorota():
    return render_template('vorota.html', title='Ворота')


@app.route('/rolets')
def rolets():
    return render_template('rolets.html', title='Рольставни')


@app.route("/barrier")
def barrier():
    return render_template('barrier.html', title='Шлагбаумы')


@app.route('/anketa', methods=['POST', 'GET'])
def anketa():
    if request.method == 'POST':
        number = request.form['number']
        name = request.form['name']
        text = request.form['text']

        data = Message(number=number, name=name, text=text)

        try:
            db.session.add(data)
            db.session.commit()
            return redirect('/')
        except:
            return 'Произошла ошибка попробуйте ещё раз'
    else:
        return render_template('anketa.html', title='Анкета')


@app.route('/admin')
def admin():
    messages = Message.query.order_by(Message.date.desc()).all()
    return render_template('admin.html', title='Просмотр сообщений', data=messages)
