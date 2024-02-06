# İçe Aktar
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_wordle = request.form.get('button_wordle')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_wordle=button_wordle, button_html=button_html, button_db=button_db)

# Geri bildirim
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    email = request.form['email']
    feedback = request.form['text']
    
    # Process the feedback (store in database, send email, etc.)
    
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == "__main__":
    app.run(debug=True)