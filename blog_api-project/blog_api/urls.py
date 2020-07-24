from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Blog API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), 
    #Here add v1 is a good practice, which means version:1
    path('api-auth/',include('rest_framework.urls')),
    #This url is for the auth of the api 
    path('api/v1/rest-auth/',include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    path('schema/',schema_view)
]
