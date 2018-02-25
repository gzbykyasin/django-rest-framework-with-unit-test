from django.db import models


class Experiment(models.Model):
    """
    Experiment Model
    """
    name = models.CharField(max_length=255,help_text='Enter the Name Surname')
    email = models.EmailField(max_length=255,help_text='Enter the Email Address')
    score = models.IntegerField(help_text='Enter the score ( 10 , 20 as )')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_email(self):
        return self.name + ' belongs to ' + self.email + ' email.'

    def __repr__(self):
        return self.name + ' is added.'
