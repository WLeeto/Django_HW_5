from rest_framework import serializers

from measurement.models import Sensor, Measurment


# TODO: опишите необходимые сериализаторы


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['date', 'temperature']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasureSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'discription', 'measurements']
