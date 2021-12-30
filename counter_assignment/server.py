from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():

    if 'num_count' not in session:
        session['num_count'] = 1
    else:
        session['num_count'] = session['num_count'] + 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


# @app.route('/test_it')
# def test_it():
#     return render_template('test_it.html')


if __name__ == "__main__":
    app.run(debug=True)