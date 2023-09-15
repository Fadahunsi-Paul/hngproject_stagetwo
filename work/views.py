from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer 

class PersonAPIview(APIView):
    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetails(APIView):
    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
