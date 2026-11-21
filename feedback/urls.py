from django.urls import path

from .views import FeedbackView, ThanksView

app_name = 'feedback'

urlpatterns = [
    path('', FeedbackView.as_view(), name='form'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]
