from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    def get(self,request):
        a=88
        b=99

        q=222
        y=333
        x = 666

        u=777

        return Response({'data':"good"})
