from application import db
from application.models import Workout, Exercises

db.drop_all()


db.create_all()
exercise1 = Exercises(exercise_name = 'Back squat')
exercise2 = Exercises(exercise_name = 'Deadlift')
exercise3 = Exercises(exercise_name = 'Bench press')

db.session.add(exercise1)
db.session.add(exercise2)
db.session.add(exercise3)
db.session.commit()
