from flask import Flask
app = Flask(__name__)
@app.route('/index')
def index():
    return 'Hello!'


app.run(debug=True)