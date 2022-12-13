# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Sensor, Measurment
from .serializers import SensorSerializer


class CreateAPIView(ListAPIView):
    def post(self, request):
        name = request.GET['name']
        discription = request.GET['discription']
        Sensor(name=name, discription=discription).save()

        return Response({'status': f'Датчик {name} добавлен'})


class RetrieveUpdateAPIView(ListAPIView):
    def patch(self, request):
        id = request.GET['id']
        sensor = Sensor.objects.get(id=id)
        if request.GET['name'] and request.GET['discription']:
            name = request.GET['name']
            sensor.name = name
            discription = request.GET['discription']
            sensor.discription = discription
            sensor.save()
            return Response({'status': f'Имя датчика {id} изменено на {name}, описание изменено на {discription}'})

        elif request.GET['name']:
            name = request.GET['name']
            sensor.name = name
            sensor.save()
            return Response({'status': f'Имя датчика {id} изменено на {name}'})

        elif request.GET['discription']:
            discription = request.GET['discription']
            sensor.discription = discription
            sensor.save()
            return Response({'status': f'Описание датчика {id} изменено на {discription}'})


class AddMeasureAPIView(ListAPIView):
    def post(self, request):
        id = request.GET['id']
        temp = request.GET['temp']
        sensor = Sensor.objects.get(id=id)
        name = sensor.name

        measurement = Measurment(temperature=temp, sensor=sensor)
        measurement.save()

        return Response({'status': f'Температура датчика {name} изменена на {temp}'})


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
