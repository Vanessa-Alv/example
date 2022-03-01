from flask import Flask, render_template  # added render_template! THIS MUST be added to connect HTML file
app = Flask(__name__)

@app.route('/play')
def idex():
    return render_template("index.html", num=3, color="blue")#input the html file here so connect both files
    
@app.route('/play/<int:num>')
def idex(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def idex(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)

