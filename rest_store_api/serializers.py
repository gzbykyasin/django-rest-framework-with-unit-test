from rest_framework import serializers
from .models import Experiment


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ('name', 'email', 'score', 'created_at', 'updated_at')
