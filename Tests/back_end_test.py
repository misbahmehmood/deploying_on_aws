import unittest

from flask import url_for 
from flask_testing import TestCase

from application import app, db
from application.models import Workout, Exercises
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLACADEMY_DATABASE_URI = getenv('TEST_FLASK_PROJECT_DB_URI'),
            SECRET_KEY = getenv('TEST_SECRET_KEY'),
            WTF_CSRF_ENABLED = False,
            DEBUG = True
        )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        #create exercises

        exercise1 = Exercises(
            exercise_name = 'Back squat'
        ) 

        exercise2 = Exercises(
            exercise_name = 'Deadlift'
        )
        exercise3 = Exercises(
            exercise_name = 'Bench press'
        )

        db.session.add(exercise1)
        db.session.add(exercise2)
        db.session.add(exercise3)
        db.session.commit()

        #Remove data after each test
        def tearDown(self):
            db.session.remove()
            db.drop_all()

class testViews(TestBase):
    def test_homepage_view(self):
        #test homepage is accessible
        homeResponse = self.client.get(url_for('home'))
        self.assertEqual(homeResponse.status_code, 200)
    
    def test_about_page(self):
        aboutResponse = self.client.get(url_for('about'))
        self.assertEqual(aboutResponse.status_code, 200)

    def test_add_workout_page(self):
        addWorkoutResponse = self.client.get(url_for('add_workout'))
        self.assertEqual(addWorkoutResponse.status_code, 200)

    def test_workouts_page(self):
        workoutsResponse = self.client.get(url_for('workouts'))
        self.assertEqual(workoutsResponse.status_code, 200)

    def test_add_workout_table(self):
        workout = Workout(
            first_name = 'testname',
            last_name = 'testlastname',
            exercise_id = 1,
            maximum_lift = 150,
            notes = 'test notes'
        )
        db.session.add(workout)
        db.session.commit()
        self.assertEqual(Workout.query.count(), 1)

class TestPosts(TestBase):
    def test_add_workout(self):
        response = self.client.post(
            '/add_workout',
            data=dict(
                first_name = 'testFirstName',
                last_name = 'testLastName',
                exercise_name = 'Back squat',
                maximum_lift = '123',
                notes = 'test notes'
            ),
            follow_redirects = True
        )
        self.assertIn(b'Great Session testFirstName', response.data)
        
        with self.client:
            response = self.client.get(url_for('post', post_id = 1))
            self.assertEqual(response.status_code, 200)
        with self.client:
            response = self.client.get(url_for('update_post', post_id = 1))
            self.assertEqual(response.status_code, 200)
        with self.client:
            response = self.client.post(
                '/post/1/update',
                 data=dict(
                first_name = 'newFirstName',
                last_name = 'testLastName',
                exercise_name = 'Back squat',
                maximum_lift = '123',
                notes = 'test notes'
            ),
            follow_redirects = True
            )
            self.assertIn(b'newFirstName', response.data)

    def test_delete_workout(self):
        response = self.client.post(
            '/add_workout',
            data=dict(
                first_name = 'testFirstName',
                last_name = 'testLastName',
                exercise_name = 'Back squat',
                maximum_lift = '123',
                notes = 'test notes'
            ),
            follow_redirects = True
        )
        self.assertIn(b'Great Session testFirstName', response.data)            
               
        with self.client:
            response = self.client.get(url_for('delete_post', post_id = 1))
            follow_redirects = True
            self.assertEqual(Workout.query.count(), 0)


        


    