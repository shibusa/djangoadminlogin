# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from loginadmin.views import sessioncheck
import socket

def index(request):
    return sessioncheck(request, render(request, 'main/index.html', {"hostname": socket.gethostname()}))
