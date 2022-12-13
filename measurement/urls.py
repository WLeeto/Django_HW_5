from django.urls import path

from measurement.views import CreateAPIView, AddMeasureAPIView, RetrieveUpdateAPIView, ListCreateAPIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('create/', CreateAPIView.as_view()),
    path('addtemp/', AddMeasureAPIView.as_view()),
    path('patch/', RetrieveUpdateAPIView.as_view()),
    path('list/', ListCreateAPIView.as_view()),

]
