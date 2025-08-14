"""
URL configuration for hlw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('topic1/', views.topic1),
    path('topic2/', views.topic2),
    path('topic3/', views.topic3),
    path('topic4/', views.topic4),
    path('topic5/', views.topic5),
    path('topic6/<str:name>/', views.topic6),
    path('topic7/', views.topic7),
    path('topic8/', views.topic8),
    path('topic9/', views.topic9),
    path('topic10/', views.topic10),
    path('topic11/', views.topic11),
    path('topic12/', views.topic12),
    path('topic13/', views.topic13),
    path('topic14set/', views.topic14_set_cookie),
    path('topic14get/', views.topic14_get_cookie),
    path('topic15/', views.topic15),
    path('topic16/', views.topic16),
    path('topic17/', views.topic17),
    path('topic18/', views.topic18),
    path('topic19/', views.topic19),
    path('topic20/', views.topic20),
    path('topic21/', views.topic21),
    path('topic22/', views.topic22),
    path('topic23/', views.topic23),
    path('topic24/', views.topic24),
    path('topic25/', views.topic25),
    path('topic26/', views.topic26),
    path('topic27/', views.topic27),
    path('topic28/', views.topic28),
    path('topic29/', views.topic29),
]