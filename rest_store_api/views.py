from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Experiment
from .serializers import ExperimentSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_experiment(request, pk):
    try:
        experiment =  Experiment.objects.get(pk=pk)
    except Experiment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single experiment
    if request.method == 'GET':
        serializer = ExperimentSerializer(experiment)
        return Response(serializer.data)
        # update details of a single experiment
    if request.method == 'PUT':
        serializer = ExperimentSerializer(experiment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single experiment
    elif request.method == 'DELETE':
        experiment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def get_post_experiments(request):
    # get all experiments
    if request.method == 'GET':
        experiments = Experiment.objects.all()
        serializer = ExperimentSerializer(experiments, many=True)
        return Response(serializer.data)
    # insert a new record for a experiment
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'email': request.data.get('email'),
            'score': int(request.data.get('score'))

        }
        serializer = ExperimentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

