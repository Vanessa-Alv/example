from flask import Flask  
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/hello/<name>') 
def hello(name):
    print(name)
    return "Hi, " + name

@app.route('/users/<string:word>/<int:num>')
def show_user_profile(word, num):
    return word * num

if __name__=="__main__":
    app.run(debug=True)