import collections
from flask import Flask,render_template,request
import os
import time



app = Flask(__name__)


@app.route("/")

def index():
    username = "none"
    username = str(request.args.get('v'))
    print(username)
    if(username == "None"):
        return render_template("none.html")
    return render_template("index.html", value=username)
    

if __name__=="__main__":
    app.run(host  = os.getenv('IP', '0.0.0.0'), 
            port  = int(os.getenv('PORT', 4904)),
            debug = True) 