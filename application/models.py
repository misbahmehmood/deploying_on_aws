from application import db



class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    maximum_lift = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(500), nullable=False)
    
    

    def __repr__(self):
     return ''.join([
         'User: ', self.first_name, ' ', self.last_name, '\r\n',
         'Exercise: ', self.exercise_id, '\r\n', self.maximum_lift, 'kg',
         'Notes: ', self.notes
         ])

class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(20), unique=True, nullable=False)
    exercise = db.relationship('Workout', backref='exercises', lazy=True)
    
       

    def __repr__(self):
        return ''.join([
            'Exercise: ', self.exercise_id, self.exercise_name
        ])


    



