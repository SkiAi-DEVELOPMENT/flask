from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'poop in fuck !'

if __name__ == '__main__':
    app.run(debug=True)


