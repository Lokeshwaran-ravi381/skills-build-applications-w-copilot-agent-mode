from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, type='run', duration=10, distance=2.5)
        self.assertEqual(activity.type, 'run')

    def test_workout_creation(self):
        workout = Workout.objects.create(user=self.user, name='Pushups', reps=20)
        self.assertEqual(workout.reps, 20)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user=self.user, score=50)
        self.assertEqual(leaderboard.score, 50)
