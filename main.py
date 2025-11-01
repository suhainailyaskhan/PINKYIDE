from flask import Flask, render_template, request
import io
import sys
from contextlib import redirect_stdout

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.form['code']
    output = io.StringIO()
    try:
        with redirect_stdout(output):
            exec(code, {})
        result = output.getvalue()
    except Exception as e:
        result = str(e)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
