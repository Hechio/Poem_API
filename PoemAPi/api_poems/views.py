from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Poem
from .serializers import PoemSerializer


# Create your views here.
@csrf_exempt
def poem_list(request):
    if request.method == "GET":
        poems = Poem.objects.all()
        serializer = PoemSerializer(poems, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PoemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def poem_detail(request, pk):
    try:
        poem = Poem.objects.get(pk=pk)

    except Poem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PoemSerializer(poem)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PoemSerializer(poem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        poem.delete()
        return HttpResponse(status=204)
