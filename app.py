from flask import Flask

app = Flask(__name__)

#@app.route('/', methods=['POST', 'GET'])
@app.route('/')

def index():
    return "Helloword!"

if __name__ == "__main__":
    app.run(debug=True)
    

