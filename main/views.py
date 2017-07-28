# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import socket

requestpath = '/'

def index(request):
    if 'user' in request.session:
        return render(request, 'main/index.html', {"hostname": socket.gethostname()})
    return redirect(requestpath)
