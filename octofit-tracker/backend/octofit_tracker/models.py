from djongo import models

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
