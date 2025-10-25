from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from uuid import uuid4
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes usando PyMongo
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.workouts.delete_many({})
        db.leaderboard.delete_many({})

        # Crear índice único en email para usuarios
        db.users.create_index('email', unique=True)

        # Crear equipos
        marvel = Team.objects.create(id=uuid4().hex, name='Marvel')
        dc = Team.objects.create(id=uuid4().hex, name='DC')

        # Crear usuarios
        users = [
            User.objects.create(id=uuid4().hex, name='Peter Parker', email='peter@marvel.com', team=marvel),
            User.objects.create(id=uuid4().hex, name='Tony Stark', email='tony@marvel.com', team=marvel),
            User.objects.create(id=uuid4().hex, name='Bruce Wayne', email='bruce@dc.com', team=dc),
            User.objects.create(id=uuid4().hex, name='Clark Kent', email='clark@dc.com', team=dc),
        ]

        # Crear actividades
        Activity.objects.create(id=uuid4().hex, user=users[0], type='Running', duration=30, date='2025-10-25')
        Activity.objects.create(id=uuid4().hex, user=users[1], type='Cycling', duration=45, date='2025-10-24')
        Activity.objects.create(id=uuid4().hex, user=users[2], type='Swimming', duration=60, date='2025-10-23')
        Activity.objects.create(id=uuid4().hex, user=users[3], type='Yoga', duration=20, date='2025-10-22')

        # Crear workouts
        Workout.objects.create(id=uuid4().hex, name='Pushups', description='Upper body', difficulty='Easy')
        Workout.objects.create(id=uuid4().hex, name='Squats', description='Lower body', difficulty='Medium')

        # Crear leaderboard
        Leaderboard.objects.create(id=uuid4().hex, team=marvel, points=150)
        Leaderboard.objects.create(id=uuid4().hex, team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
