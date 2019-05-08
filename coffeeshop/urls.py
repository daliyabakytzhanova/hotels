from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from coffeeshop import settings
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('hotel_list', HotelListView.as_view(), name="hotel_list"),
    path('zakaz/',zakaz),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)