from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.main_frame, name='main_frame'),
    #path('<str:arg1>/', views.main_frame, name='main_frame'),
    path('<str:arg1>/<str:arg2>/<int:signal1>/<int:signal2>', views.main_frame, name='main_frame'),
    path('<str:arg1>/<str:arg2>/<str:input>/<str:output>', views.show, name='show'),
    path('<str:arg1>/<str:arg2>/<int:signal1>/<int:signal2>/', views.main_frame, name='main_frame'),
    path('<str:arg1>/<str:arg2>/<int:signal1>/<int:signal2>/<str:favorite>', views.main_frame, name='main_frame'),
    path('switch_text/<str:arg1>/<str:arg2>', views.switch_text, name='switch_text'),
    path('switch_file/<str:arg1>/<str:arg2>', views.switch_file, name='switch_file'),
    path('<int:args>/', views.main_frame, name='main_frame'),
    path('translate/<str:arg1>/<str:arg2>/', views.translate, name='translate'),
    path('add_favorite/<str:arg1>/<str:arg2>/<str:input>/<str:output>', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<str:arg1>/<str:arg2>/<str:input>/<str:output>/<int:id>', views.remove_favorite, name='remove_favorite'),
    path('clear_history/<str:arg1>/<str:arg2>/', views.clear_history, name='clear_history'),
    path('clear_selected/<str:arg1>/<str:arg2>/', views.clear_selected, name='clear_selected'),
    path('documents/', views.documents, name='documents'),
    path('documents/<str:arg1>/<str:arg2>/<int:signal1>/<int:signal2>', views.documents, name='documents'),
    path('about/', views.about, name='about'),
    path('read_file/', views.read_file, name='read_file'),
    path('read_file/<str:arg1>/<str:arg2>', views.read_file, name='read_file'),
    path('hello/', views.hello, name='hello'),
    path('send_report/', views.send_report, name='send_report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)