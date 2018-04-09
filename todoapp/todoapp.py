from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aljamil:limajla@localhost/todoapp'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from view import *

if __name__ == '__main__':
	app.run(debug = True)

