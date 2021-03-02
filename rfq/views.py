from django.shortcuts import render
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import Listofrfqserializer
from rest_framework import permissions
from .models import Rfq
# Create your views here.
from rest_framework.response import Response


class ListofrfqView(APIView):
    permissions=[permissions.IsAuthenticated,]
    serializer_class=Listofrfqserializer


    def get(self,request):
        user=request.user
        queryset=Rfq.objects.all().filter(user_id=user)
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)





