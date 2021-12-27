from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

#ImmutableMultiDict
#([('player1_name', 'Amani'),
#('player1_move', 'scissors'),
#('player2_name', 'Sheena'),
#('player2_move', 'rock')])

@app.route('/process_form', methods=['POST'])
def process_form():
    session['data']=request.form
    #print(request.form['player1_name'])

    return redirect('/result')

@app.route('/result')
def result():

    result = ''
    player1Move=session['data']['player1_move']
    player2Move=session['data']['player2_move']

    if player1Move == 'rock' and player2Move == 'scissors':
        result = 'Player 1 Wins!'
    elif player1Move == 'scissors' and player2Move == 'rock':
        result = 'Player 2 Wins!'
    elif player1Move == 'scissors' and player2Move == 'paper':
        result = 'Player 1 Wins!'
    elif player1Move == 'paper' and player2Move == 'scissors':
        result = 'Player 2 Wins!'
    elif player1Move == 'paper' and player2Move == 'rock':
        result = 'Player 1 Wins!'
    elif player1Move == 'rock' and player2Move == 'paper':
        result = 'Player 2 Wins!'
    elif player1Move == player2Move:
        result = 'Tie!'

    return render_template('results.html', player1_name=session['data']['player1_name'], player2_name=session['data']['player2_name'], result = result)

if __name__ == "__main__":
    app.run(debug=True)