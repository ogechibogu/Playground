from flask import Flask, render_template
import os

app = Flask(__name__)
@app.route('/')

def main():
    background = os.environ.get('background')
    version = os.environ.get('version')
    return render_template('index.html', background=background, version=version)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
