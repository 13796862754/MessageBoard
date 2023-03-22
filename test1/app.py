from flask import Flask, render_template, request
import time

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/post/add', methods=['POST'])
def add():
    message = request.form['message']
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    messages.append((message, timestamp))
    return '', 204

if __name__ == '__main__':
    app.run()