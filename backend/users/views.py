from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from users.models import Users, CustomUserDetailsSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class GetUserView(ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = CustomUserDetailsSerializer
	http_method_names = ['get', ]
	#primary_key = ["email"]#"email"
        
	def list(self, request):
		items = self.get_queryset()
		params = request.query_params
		pp = params.dict()
		if params:
			item = self.get_queryset().filter(**pp)
			if item.exists():
				return Response(status=status.HTTP_200_OK, data={"exists": True})
			else:
				return Response( status=status.HTTP_404_NOT_FOUND, data={"exists": False})
		else:
			ser = self.get_serializer(items, many=True)
			return Response({"data": ser.data })



