from flask import Flask

'''
it creates an instance of the Flask class,
which will be yout WSGI(web serevr gatewAY INTERFACE) application

'''


app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this best flask course.this is amazing course"

@app.route("/index")
def index():
    return "this is index page"

if __name__=="__main__":
    app.run(debug=True)