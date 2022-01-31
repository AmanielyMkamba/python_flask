from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

db = "dojo_survey_schema"

class Survey:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.location=data["location"]
        self.language=data["language"]
        self.comment=data["comment"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def create_survey(cls, data):
        query = """INSERT INTO dojos (name, location, language, comment)
                    VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_survey(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @staticmethod
    def survey_validation(data):
        is_valid = True
        if len(data["name"]) < 3:
            is_valid = False
            flash("Name has to be at least 3 characters")
        if len(data["location"]) < 1:
            is_valid = False
            flash("Must choose a dojo lacation")
        if len(data["language"]) < 1:
            is_valid = False
            flash("Must choose a favorite language")
        if len(data["comment"]) < 3:
            is_valid = False
            flash("Comment has to be at least 3 characters")
        return is_valid