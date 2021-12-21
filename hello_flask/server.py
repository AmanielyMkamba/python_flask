from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dessert/<name>')
def dessert(name):
    return f'{name} is fantastic'

@app.route('/person/<string:first_name>') #By default is a string

def person(first_name):
    return f'Welcome {first_name.capitalize()} to Today!'

@app.route('/dessert/<int:x>/<int:y>')
def dessert_count(x,y):
    sum = x + y
    return str(sum)

# @app.route('/pie_list')
# def pie_list():
#     return render_template('index.html', pie_list = ['Apple', 'Cherry', 'Potato'])

@app.route('/num_list')
def num_list():
    return render_template('index.html', num = 5)

@app.route('/num_list/<int:num>')
def num_qty(num):
    return render_template('index.html', num = num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

