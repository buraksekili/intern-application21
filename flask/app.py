from flask import Flask
import socket

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/staj', methods=['GET'])
def hello_world():
    print(socket.gethostbyname(socket.gethostname()))
    return 'Hello World from Flask!\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
      