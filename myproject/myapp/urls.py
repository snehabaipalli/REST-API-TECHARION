from django.urls import path
from .views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getdata/',get_data),
    path('postdata/',post_data),
    path('update/<int:id>/',update_data),
    path('delete/<int:id>/',delete_data),
    path('marks/<int:id>/',get_marks),
    path('postmarks/',post_marks),
]
