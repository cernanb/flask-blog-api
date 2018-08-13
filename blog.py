from flask import Flask, render_template, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

posts = [
  {
    'author': 'Cernan Bernardo',
    'title': 'Blog Post 1',
    'content': 'This is my first post',
    'date_posted': 'April 20, 2018'
  },
  {
    'author': 'Ashley Bernardo',
    'title': 'Blog Post 2',
    'content': 'This is my cool post',
    'date_posted': 'April 21, 2018'
  }
]

@app.route('/')
@app.route('/home')
def home():
  

@app.route('/about')
def about():
  return render_template('about.html', title="About")

@app.route('/posts', methods=['POST, GET'])
def posts():
  if request.method == 'GET':
    return jsonify(posts)

if __name__ == '__main__':
  app.run(debug=True)