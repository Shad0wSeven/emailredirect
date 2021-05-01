import collections
from flask import Flask,render_template,request
import os
import time



app = Flask(__name__)


@app.route("/")

def index():
    email = "None"
    email = str(request.args.get('v'))
    # print(username)
    if(email == "None"):
        return render_template("none.html")
    else:
        emailURL = f'mailto:{email}'
    return render_template("index.html", value=email, mailTo = emailURL)

@app.route("/create", methods=['post', 'get'])
def create():
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        # print(username)
        return render_template('finished.html', email=f'https://redirectemail.vercel.app/?v={username}')
    return render_template('create.html')




if __name__=="__main__":
    app.run(host  = os.getenv('IP', '0.0.0.0'), 
            port  = int(os.getenv('PORT', 4904)),
            debug = True) 