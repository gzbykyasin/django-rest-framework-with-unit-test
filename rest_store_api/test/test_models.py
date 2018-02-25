from django.test import TestCase
from ..models import Experiment


class ExperimentTest(TestCase):
    """ Test module for Experiment model """

    def setUp(self):
        Experiment.objects.create(
            name='Project', email='project@project.com',score=1)
        Experiment.objects.create(
            name='Project 2', email='project2@project.com', score=2)

    def test_experiment_email(self):
        experiment_project = Experiment.objects.get(name='Project')
        experiment_project_2 = Experiment.objects.get(name='Project 2')
        self.assertEqual(
            experiment_project.get_email(), "Project belongs to project@project.com email.")
        self.assertEqual(
            experiment_project_2.get_email(), "Project 2 belongs to project2@project.com email.")
