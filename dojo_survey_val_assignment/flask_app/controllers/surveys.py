from flask import request, render_template, redirect

from flask_app import app

from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_survey', methods=['POST'])
def process_survey():
    survey_data = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }

    valid = Survey.survey_validation(survey_data)

    if valid:
        results = Survey.create_survey(survey_data)
        return redirect(f'/results/{results}')
    return redirect('/')

@app.route('/results/<int:survey_id>')
def get_survey(survey_id):
    data = {
        "id" : survey_id
        }
    survey = Survey.get_survey(data)
    return render_template('results.html', survey = survey)