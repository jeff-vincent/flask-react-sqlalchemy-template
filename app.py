from flask import Flask, request, render_template
from config import app, db
import base_api


""" Requests from web_user """

@app.route('/', methods=['GET'])
def render_index():
    return render_template('index.html')


""" Write to MySQL """


""" ----- User Stuff ----- """

@app.route('/signup-db', methods=['POST'])
def sign_up_db():
    return base_api._create_db_user(db)

@app.route('/delete-db', methods=['POST'])
def delete_user_db():
    return base_api._delete_db_user(db)

@app.route('/login-db', methods=['POST'])
def login_user_db():
    return base_api._login_db_user(db)

@app.route('/logout-db', methods=['POST'])
def logout_user_db():
    return base_api._logout_db_user(db)



""" ----- Question and Answer Stuff ----- """

@app.route('/ask-question', methods=['POST'])
def ask_question():
    return base_api._ask_question(db)

@app.route('/answer-question', methods=['POST'])
def handle_answer():
    return base_api._answer_question(db)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
