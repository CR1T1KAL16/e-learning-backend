from django.shortcuts import render
import uuid


def jitsi_room(request):
    room_name = uuid.uuid4().hex
    return render(request, "jitsi_room.html", {"room_name": room_name})
