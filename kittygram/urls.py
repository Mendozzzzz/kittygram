# from django.urls import include, path

# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]

from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet

# Создаётся роутер
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register('api/v1/cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
] 