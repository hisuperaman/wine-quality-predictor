from rest_framework.serializers import Serializer, FloatField


class WineSerializer(Serializer):
    fixed_acidity = FloatField()
    volatile_acidity = FloatField()
    citric_acid = FloatField()
    residual_sugar = FloatField()
    chlorides = FloatField()
    free_sulfur_dioxide = FloatField()
    total_sulfur_dioxide = FloatField()
    density = FloatField()
    ph = FloatField()
    sulphates = FloatField()
    alcohol = FloatField()