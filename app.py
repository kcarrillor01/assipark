from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def users():  # put application's code here
    return render_template('users.html')


if __name__ == '__main__':
    app.run()
