from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "secretKey"

@app.route('/')
def index():
    if "goldTotal" in session:
        session["goldTotal"] = 0
    if "returnStr" in session:
        session["returnStr"] = ""
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money_farm():

    if "goldTotal" not in session:
        session["goldTotal"] = 0
    if "returnStr" not in session:
        session["returnStr"] = ""

    randList = [(10,20), (5,10), (2,5), (-50,50)]
    buildingList = ["farm", "cave", "house", "casino"]

    if request.form["gold"] == "casino":
            goldEarned = random.randint(-50,50)
            if goldEarned <= 0:
                session["returnStr"] += "<p class='red'>Entered a casino and lost " + str(goldEarned) + " gold... Ouch..</p>"
            else:
                session["returnStr"] += "<p class='green'>Entered a casino and won " + str(goldEarned)+"!<p>"
    
    else:
        for i in range (0,len(randList)):
            if request.form["gold"] == buildingList[i]:
                goldEarned = random.randint(randList[i][0], randList[i][1])
                session["returnStr"] += "<p class='green'>Earned " + str(goldEarned) + " from the " + buildingList[i] + "</p>"


    session["goldTotal"] += goldEarned

    return render_template('index.html', goldEarned=goldEarned)


if __name__=="__main__":
    app.run(debug=True)