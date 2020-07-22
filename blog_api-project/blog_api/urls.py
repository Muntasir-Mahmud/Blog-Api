from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), 
    #Here add v1 is a good practice, which means version:1
    path('api-auth/',include('rest_framework.urls')),
    #This url is for the auth of the api 
    path('api/v1/rest-auth/',include('rest_auth.urls')),
]
