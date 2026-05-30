from flask import Flask, render_template, request

app = Flask(__name__)

question = "What is Machine Learning?"

@app.route('/')
def home():
    return render_template('index.html', question=question)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    answer = request.form.get('answer', '')
    score = len(answer.split())

    if score < 10:
        feedback = "Answer is too short. Add more details."
    elif score < 30:
        feedback = "Good answer. Try adding examples."
    else:
        feedback = "Excellent answer."

    return render_template('index.html', question=question, feedback=feedback)