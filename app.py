#!/usr/bin/env python
# coding: utf-8

# In[22]:


from flask import Flask


# In[23]:


app = Flask(__name__)


# In[24]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBSReg")
        pred = model.predict([[float(rates)]])
        s = "Predicted DBS Share price based on Linear Regression model is: " + str(pred)
        model = joblib.load("DBSDT")
        pred = model.predict([[float(rates)]])
        s_dt = "Predicted DBS Share price based on Decision Tree model is " + str(pred)
        model = joblib.load("DBSNN")
        pred = model.predict([[float(rates)]])
        s_nn = "Predicted DBS Share price based on Neural Network model is " + str(pred)
        return(render_template("index.html", result1=s, result2=s_dt, result3=s_nn))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




