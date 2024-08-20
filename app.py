from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

USER_ANSWERS = []
ANSWERS = [None, 'a', 'b', 'b', 'b', 'c', 'd', 'a', 'b', 'a', 'a', 'c', 'b', 'b', 'a', 'b', 'd', 'c', 'c', 'd', 'd', 'd', 'd', 'a', 'a', 'c', 'b', 'c']
USER_EMAIL = 'example@gmail.com'
USER_NAME = 'example'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/question", methods=['GET', 'POST'])
def question():
    if request.method == "POST":
        global USER_NAME
        USER_EMAIL = request.form.get("email")
        USER_NAME = request.form.get("name")
        print(USER_EMAIL, USER_NAME)
        return render_template('question.html')
    else:
        return render_template("index.html")


@app.route('/process_array', methods=['POST'])
def process_array():
    global USER_ANSWERS
    data = request.get_json()  # Receive the JSON data
    USER_ANSWERS = data.get('data')   # Extract the array from the received JSON
    n = 28 - len(USER_ANSWERS)
    for i in range(n):
        USER_ANSWERS.append(None)
    # Process the array as needed
    print(USER_ANSWERS)
    result = 12
    return jsonify({'resul2t': result})  # Return a JSON response

@app.route("/results", methods=['GET', 'POST'])
def results():
    global USER_NAME
    global USER_ANSWERS
    print(USER_ANSWERS)
    cnt = 0
    for i in range(27):
        if USER_ANSWERS[i+1] == ANSWERS[i+1]:
            cnt += 1
    return render_template('result.html', name = USER_NAME, USER_ANSWERS = USER_ANSWERS, ANSWERS = ANSWERS, cnt = cnt)
