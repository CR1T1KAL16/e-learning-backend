from django.urls import path
from .views import jitsi_room

urlpatterns = [
    path("jitsi-meet/", jitsi_room, name="jitsi_room"),
]
