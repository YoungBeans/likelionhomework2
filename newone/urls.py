
import wordcount.views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name='home'),
    path('about/', wordcount.views.about, name='about'),
    path('result/', wordcount.views.result, name='result'),
    path('board/', include('board.urls'), name='board')
]
