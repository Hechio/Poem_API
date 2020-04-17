from django.http import HttpResponse, JsonResponse
from .models import Poem
from .serializers import PoemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins


# Create your views here.


# Generic api view
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin
                     , mixins.DestroyModelMixin):
    serializer_class = PoemSerializer
    queryset = Poem.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


# Class based api view
class PoemAPIView(APIView):
    def get(self, request):
        poems = Poem.objects.all()
        serializer = PoemSerializer(poems, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PoemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PoemDetails(APIView):
    def get_object(self, id):
        try:
            return Poem.objects.get(id=id)

        except Poem.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        poem = self.get_object(id)
        serializer = PoemSerializer(poem)
        return Response(serializer.data)

    def put(self, request, id):
        poem = self.get_object(id)
        serializer = PoemSerializer(poem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        poem = self.get_object(id)
        poem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# function based api view
@api_view(['GET', 'POST'])
def poem_list(request):
    if request.method == "GET":
        poems = Poem.objects.all()
        serializer = PoemSerializer(poems, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PoemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def poem_detail(request, pk):
    try:
        poem = Poem.objects.get(pk=pk)

    except Poem.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PoemSerializer(poem)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PoemSerializer(poem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        poem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
