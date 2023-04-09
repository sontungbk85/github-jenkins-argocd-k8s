from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Xin chào, hôm nay là ngày 08.02.2023'

if __name__ == '__main__':
    app.run()
