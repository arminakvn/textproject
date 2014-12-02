from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'index page!'

@app.route('/home')
def home():
	return 'home page!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')