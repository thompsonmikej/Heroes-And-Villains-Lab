from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SuperSerializer
from rest_framework import status
from .models import Super
from supers.models import Super

# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        hero_or_villain = request.query_params.get('type') #filters the URL inquiry by "?type=" to one specific response
        print(hero_or_villain)  #"?type=" returns "hero" or "villain"
        supers = Super.objects.all() #pulls the super characters
        
        if  hero_or_villain: #if this parameter has a value: hero or villain
            supers = supers.filter(super_type__type = hero_or_villain) #filter super characters 
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE']) 
def supers_detail(request, pk):
    supers= get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(supers) 
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET']) 
def supers_list(request):
    the_supers_collection = {}
    the_supers_collection['name'] = '' #should it not pull names from the DB?
    print (the_supers_collection) # {'name': 'Mighty Mouse'}

    supers = Super.objects.all() #pulls in all supers

    custom_response = {'heroes': [], 'villains':[] }
    # custom_response = 0

    for type in super_types:
        supers = supers.filter(super_types__id=type.id)
        serializer = SuperSerializer(supers, many=True)
        
        custom_response [super.name] = { 
            "name": super.name, "supers": serializer.data
            }
    return Response(custom_response)