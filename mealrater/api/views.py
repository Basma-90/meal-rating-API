from django.shortcuts import render
from .serializers import MealSerializer,RatingSerializer
from .models import Meal,Rating
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework import permissions
# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(AllowAny,)

class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
    #authentication_classes=(TokenAuthentication,)
    #permission_classes=(IsAuthenticated,)

    def update(self,request,*args,**kwargs):
        response={'message':'you cant update rating like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    def create(self,request,*args,**kwargs):
        response={'message':'you cant create rating like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

@action(detail=True,methods=['POST'])
def rate_meal(self,request,pk=None) :
    if 'stars' in request.data:
        meal=Meal.objects.get(id=pk)
        user=request.user
        stars=request.data['stars']

        try:
            rating=Rating.objects.get(user=user.id,meal=meal.id)
            rating.stars=stars
            rating.save()
            serializer=RatingSerializer(rating,many=False)
            response={'message':'Rating updated','result':serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            rating=Rating.objects.create(user=user,meal=meal,stars=stars)
            serializer=RatingSerializer(rating,many=False)
            response={'message':'Rating created','result':serializer.data}
            return Response(response, status=status.HTTP_200_OK)
    else:
        return Response({'message':'you need to provide stars'}, status=status.HTTP_400_BAD_REQUEST)

