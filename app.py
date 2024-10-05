from flask import Flask, render_template, request 
import google.generativeai as genai  
import os
import numpy as np
import textblob

model = genai.GenerativeModel("gemini-1.5-flash")
api = os.getenv("GEMINI")
genai.configure(api_key=api) 

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
 
@app.route("/faq", methods=["GET","POST"])
def faq():   
    return(render_template("faq.html"))

@app.route("/predict_creditability", methods=["GET","POST"])
def predict_creditability():   
    return(render_template("predict_creditability.html"))

@app.route("/predict_creditability_result", methods=["GET","POST"])
def predict_creditability_result():   
    q= float(request.form.get("q")) 
    r= -0.00010995*q + 1.15088102
    result = np.where(r>=0.5,"Creditable","Not Creditable")
    return(render_template("predict_creditability_result.html", r=result))

@app.route("/sentiment_analysis", methods=["GET","POST"])
def sentiment_analysis():   
    return(render_template("sentiment_analysis.html"))

@app.route("/sentiment_analysis_result", methods=["GET","POST"])
def sentiment_analysis_result():  
    q= request.form.get("q")
    r= textblob.TextBlob(q).sentiment.polarity  
    result = np.where(r>=0,"Positive","Negative")
    return(render_template("sentiment_analysis_result.html", r=result))

@app.route("/q1", methods=["GET","POST"])
def q1(): 
    r = model.generate_content("How should i diversify my investment portfolio?")  
    return(render_template("q1_reply.html", r=r))

@app.route("/q2", methods=["GET","POST"])
def q2():   
    q = request.form.get("q")
    r = model.generate_content(q).text
    return(render_template("q2_reply.html", r=r))

if __name__ == "__main__": 
    app.run(port=1234) #to change port number: app.run(port=1234)

  