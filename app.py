from flask import Flask, render_template, request 

app = Flask(__name__)

#@ > decorator is run before the method definition
@app.route("/", methods=["GET","POST"])
def index(): 
    return(render_template("index.html"))

@app.route("/prediction_DBS", methods=["GET","POST"])
def prediction_DBS(): 
    return(render_template("prediction_DBS.html"))

@app.route("/prediction_DBS_result", methods=["GET","POST"])
def prediction_result_DBS(): 
    q= float(request.form.get("q"))
    r= -50.6*q + 90.2
    return(render_template("prediction_DBS_result.html", r=r))

if __name__ == "__main__": 
    app.run() #to change port number: app.run(port=1234)




