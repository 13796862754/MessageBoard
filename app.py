from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.jinja2', messages=messages)

@app.route('/post/add', methods=['POST'])
def add_message():
    messages.append({
        'text': request.form['message_text'],
        'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })
    return index()

if __name__ == '__main__':
    app.run(debug=True)



