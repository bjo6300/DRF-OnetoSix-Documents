from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# router를 생성하고 viewset을 등록한다
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API URL은 router에 의해 자동적으로 결정되어진다
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]