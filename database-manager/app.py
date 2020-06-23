from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome

app=Flask(__name__)
bootstrap=Bootstrap(app)
fa=FontAwesome(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flask_masterclass'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), nullable=False, unique=True, index=True)
	password = db.Column(db.String(255), nullable=False, index=True)

	def __str__(self):
		return self.name

@app.route('/')
def redirectUsers():
	return redirect('/users')

@app.route('/users')
def index():
	users = User.query.all()
	return render_template('/users.html', users=users)

@app.route('/user/<int:id>')
def unique(id):
	user = User.query.get(id)
	return render_template("user.html", user=user)

@app.route('/user/delete/<int:id>')
def delete(id):
	user = User.query.filter_by(id=id).first()
	db.session.delete(user)
	db.session.commit()
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)