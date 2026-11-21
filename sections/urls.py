from django.urls import path
from django.views.generic import RedirectView

from .views import SectionView, SubsectionView

app_name = 'sections'

urlpatterns = [
    path('', SectionView.as_view(section='home'), name='home'),
    path('news/', SectionView.as_view(section='news'), name='news'),
    path('management/', SectionView.as_view(section='management'), name='management'),
    path('about/', SectionView.as_view(section='about'), name='about'),
    path('contacts/', SectionView.as_view(section='contacts'), name='contacts'),
    path('contact/', RedirectView.as_view(pattern_name='sections:contacts', permanent=True)),

    path('<slug:section>/<slug:slug>/', SubsectionView.as_view(), name='subsection'),
]
