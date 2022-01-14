from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/second-route', methods=['POST'])
def second():
    username = request.form['username']
    password = request.form['password']

    print(username, password)

    result = 'username: ' + username + '<br />password: ' + password

    return result

if __name__ == '__main__':
    app.run()