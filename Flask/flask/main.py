from flask import Flask,render_template

'''
it creates an instance of the Flask class,
which will be yout WSGI(web serevr gatewAY INTERFACE) application

'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to this flask course</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)