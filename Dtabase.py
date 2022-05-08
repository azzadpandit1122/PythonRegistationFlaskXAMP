from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/coding thunder'
db = SQLAlchemy(app)


class Contactw(db.Model):
    sno = db.Column(db.Integer, unique=True, nullable=False)
    msg = db.Column(db.String(90), primary_key=True)
    name = db.Column(db.String(12), unique=False, nullable=False)
    date = db.Column(db.String(11), unique=False, nullable=False)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        msg = request.form.get('msg')
        date = request.form.get('date')

        entry = Contactw(name=name, msg=msg, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return render_template('Successful.html')

    return render_template('index.html')


app.run(debug=True, port=900)
