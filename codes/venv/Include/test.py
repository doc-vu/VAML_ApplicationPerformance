from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/dataview')
def data_view():
    return render_template('test.html')

@app.route('/')
def main_view():
    return render_template("subplot.html")

if __name__ == '__main__':
    app.run()