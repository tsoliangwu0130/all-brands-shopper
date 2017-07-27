from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    my_name = 'Tso-Liang'
    return render_template('index.html', my_name=my_name)


if __name__ == '__main__':
    app.run()
