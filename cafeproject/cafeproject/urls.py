from django.contrib import admin
from django.urls import path
from cafeapp import views # cafeapp에 있는 views 사용


urlpatterns = [
    path('admin/', admin.site.urls), #주소뒤에 admin있으면 admin.site.urls 띄우기
    path('', views.home, name = 'home'), # 아무것도 작성 안하고 주소 실행 시 views.home
    path('detail/', views.detail, name='detail'),
]
