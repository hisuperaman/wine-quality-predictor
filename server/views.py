from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
import joblib
import pandas as pd
from server.serializers import WineSerializer

model = joblib.load('models/red_wine_predictor.pkl')

class WineViewSet(ViewSet):
    @action(detail=False, methods=['post'])
    def predict(self, request):
        serializer = WineSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            columns = [
                "alcohol", "sulphates", "pH", "density",
                "total sulfur dioxide", "free sulfur dioxide",
                "chlorides", "residual sugar", "citric acid",
                "volatile acidity", "fixed acidity"
            ]
            row = [
                data['alcohol'],
                data['sulphates'],
                data['ph'],
                data['density'],
                data['total_sulfur_dioxide'],
                data['free_sulfur_dioxide'],
                data['chlorides'],
                data['residual_sugar'],
                data['citric_acid'],
                data['volatile_acidity'],
                data['fixed_acidity']
            ]

            df = pd.DataFrame([row], columns=columns)
            pred = model.predict(df)
            return Response({'data': {'quality': pred[0]}}, status=200)
        return Response({'error': serializer.errors}, status=400)
    