from django.contrib import admin
from django.urls import include, path, re_path

from sections.views import NotFoundView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),
    path('', include('sections.urls')),
    re_path(r'^.*/$', NotFoundView.as_view()),
]

handler404 = NotFoundView.as_view()
