from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def users():  # put application's code here
    return render_template('users.html')

@app.route('/apartments/')
def apartments():
    return render_template('apartments.html')

@app.route('/parking/')
def parking():
    return render_template('parking.html')

if __name__ == '__main__':
    app.run('')