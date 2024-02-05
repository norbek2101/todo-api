from todo.models import Task
from todo.serializers import TodoSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from drf_yasg.utils import swagger_auto_schema


class TaskListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="List of Tasks",
        responses={200: TodoSerializer(many=True)},
        tags=['Tasks'],
    )
    def get(self, request):
        user_id = request.user.id
        # task = Task.objects.all().filter(user__id=user_id)
        task = Task.objects.all()
        serializer = TodoSerializer(task,  many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body= TodoSerializer,
        operation_description="Add Single Task",
        responses={201: TodoSerializer()},
        tags=['Tasks'],
    )
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Get single Task",
        responses={200: TodoSerializer()},
        tags=['Tasks'],
    )
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TodoSerializer(task)
        return Response(serializer.data)
    

    @swagger_auto_schema(
        operation_description="Update the task",
        responses={206: TodoSerializer()},
        tags=['Tasks'],
    )
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TodoSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_206_PARTIAL_CONTENT)

    @swagger_auto_schema(
        operation_description="Delete the task",
        responses={204: TodoSerializer()},
        tags=['Tasks'],
    )
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_200_OK)


class TasksbyUser(APIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer

    @swagger_auto_schema(
        tags=['Tasks'],
    )
    def get (self, request, id):
        tasks = Task.objects.all().filter(user=id)
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)

