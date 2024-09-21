from flask import Flask, render_template, request 

app = Flask(__name__)

#@ > decorator is run before the method definition
@app.route("/", methods=["GET","POST"])
def index(): 
    return(render_template("index.html"))

if __name__ == "__main__": 
    app.run() #to change port number: app.run(port=1234)




