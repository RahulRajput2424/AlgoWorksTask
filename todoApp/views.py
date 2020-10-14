import datetime
from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView,\
                                    ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .serializers import UserSignupSerializer, UserLoginSerializer,AddTodoSerializer, ListTodoSerializer,AddCommnetSerializer,\
    AddReplySerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .models import User, ToDo, Comment
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status, serializers, authentication
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from todoApp.permission import AdminPermission


class UserSignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Successfully Created, Please Sign-In`',
            'data': response.data
        })
    
class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token= Token.objects.get_or_create(user=user)
            response = {"data": {"message":"You have logged in successfully.",
													  "token": str(token), 
										},
								"status": 200,}
            return Response(response, status=status.HTTP_200_OK)
        else:
            error_data = serializer.errors
            return Response(data=error_data)

class AddTodoView(generics.CreateAPIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = AddTodoSerializer

	def create(self, request):
		request.data['user'] = request.user.id
		response = super().create(request)
		return Response({
            'status': 200,
            'message': 'Successfully Created',
            'data': request.data
        })


class EditToDoView(generics.UpdateAPIView):
	queryset = ToDo.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = AddTodoSerializer

	def update(self, request, pk):
		request.data['user'] = request.user.id
		response = super().update(request)
		return Response({
            'status': 200,
            'message': 'ToDo has been successfully updated',
            'data': request.data
        })


class ToDoListView(generics.ListAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = ToDo.objects.all()
	serializer_class = ListTodoSerializer
	pagination_class = PageNumberPagination

	def get_queryset(self):
		queryset = ToDo.objects.filter(user_id=self.request.user.id)
		data_list = []
		for val in queryset:
			status_context_dict = {}
			status_context_dict["user"] = self.request.user.username
			status_context_dict["name"] = val.name
			status_context_dict["end_date"] = val.end_date
			if val.end_date < datetime.datetime.now(tz=datetime.timezone.utc):
				status = "expired date is crossed"
			else:
				status = "expired date is not crossed"
			status_context_dict["status"] = status
			data_list.append(status_context_dict)
		return data_list

class DeleteToDoView(generics.DestroyAPIView):
	queryset = ToDo.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = AddTodoSerializer

	def delete(self, request, pk):
		response = super().delete(request)
		return Response({
            'status': 200,
            'message': 'Successfully deleted',
            'data': request.data
        })
class AddComment(generics.CreateAPIView):

	queryset = ToDo.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = AddCommnetSerializer

	def create(self, request, pk):
		instance = get_object_or_404(ToDo, pk=pk)
		request.data["todo"] = instance.id
		response = super().create(request)
		return Response({
            'status': 200,
            'message': 'Successfully Created.',
            'data': request.data
        })

class AddReply(generics.CreateAPIView):

	queryset = Comment.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = AddReplySerializer

	def create(self, request, pk):
		instance = get_object_or_404(Comment, pk=pk)
		request.data["comment"] = instance.id
		response = super().create(request)
		return Response({
            'status': 200,
            'message': 'Successfully Created.',
            'data': request.data
        })

class AdminToDoListView(generics.ListAPIView):
	permission_classes = (IsAuthenticated, AdminPermission)
	queryset = ToDo.objects.all()
	serializer_class = ListTodoSerializer
	pagination_class = PageNumberPagination

	def get_queryset(self):
		queryset = ToDo.objects.all()
		data_list = []
		for val in queryset:
			status_context_dict = {}
			status_context_dict["name"] = val.name
			if val.user:
				status_context_dict["user"] = val.user.username
			else:
				status_context_dict["user"] = ""
			status_context_dict["end_date"] = val.end_date
			if val.end_date < datetime.datetime.now(tz=datetime.timezone.utc):
				status = "expired date is crossed"
			else:
				status = "expired date is not crossed"
			status_context_dict["status"] = status
			data_list.append(status_context_dict)
		return data_list