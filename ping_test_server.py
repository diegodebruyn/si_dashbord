import subprocess
from flask import Flask
import ping_test

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return ping_test()


@app.route('/x')
def hello_world_2():
    return 'Hello, World 3!'
 
app.run(debug=True, port=5000)





