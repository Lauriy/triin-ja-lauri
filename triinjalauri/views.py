from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    context = {}

    return render_to_response('home.html', RequestContext(request, context))


def where(request):
    context = {}

    return render_to_response('where.html', RequestContext(request, context))


def gallery(request):
    context = {}

    return render_to_response('gallery.html', RequestContext(request, context))


def transport(request):
    context = {

    }

    return render_to_response('transport.html', RequestContext(request, context))


def faq(request):
    context = {}

    return render_to_response('faq.html', RequestContext(request, context))
