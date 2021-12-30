from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    session['data'] = request.form

    return redirect('/result')

@app.route('/result')
def result():

    return render_template('results.html', user_name=session['data']['user_name'], dojo_location=session['data']['dojo_location'], fav_language=session['data']['fav_language'], comment=session['data']['comment'], result = result)

if __name__ == "__main__":
    app.run(debug=True)
