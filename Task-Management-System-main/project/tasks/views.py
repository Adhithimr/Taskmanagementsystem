from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .services import TaskService
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

@api_view(['GET', 'POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'api/tasks/')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, "register.html")
   
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            html_content = f"""
            <html>
            <head>
            <meta http-equiv="refresh" content="0;url=/api/tasks/">
            </head>
            <body>
            <p>You are being redirected to /api/tasks/...</p>
            <p>Access Token: {access_token}</p>
            </body>
            </html>
            """
            return HttpResponse(html_content)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return render(request, 'login.html')

class TaskListCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        completed = request.query_params.get('completed')
        if completed is not None:
            if completed.lower() == 'true':
                completed_bool = True
            elif completed.lower() == 'false':
                completed_bool = False
            else:
                return Response({"error": "Invalid completed parameter. Use true or false."}, status=status.HTTP_400_BAD_REQUEST)
            tasks = TaskService.get_all_tasks(completed=completed_bool)
        else:
            tasks = TaskService.get_all_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = TaskService.create_task(**serializer.validated_data)
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get(self, request, task_id):
        task = TaskService.get_task_by_id(task_id)
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, task_id):
        serializer = TaskSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            task = TaskService.update_task(task_id, **serializer.validated_data)
            if task:
                return Response(TaskSerializer(task).data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        if TaskService.delete_task(task_id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

# Create your views here.
