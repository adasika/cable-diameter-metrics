from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cable
from .serializer import Cable_Serializer
from .tasks import get_cable_data


#the main function rendering to our react app
class Front_End_View(APIView):
    get_cable_data.delay()
    serializer = Cable_Serializer   
    #won't be needing POST request as frontend only needs to get data
    def get(self, request):
        #sending frontend info in JSON format
        cable_info = [{'time_stamp': a.time_stamp, 'minimum': a.minimum, 'average': a.average, 'maximum': a.maximum}
        for a in Cable.objects.all()]

        return Response(cable_info)


# def index(request):
#     return render(request, 'index.html')
