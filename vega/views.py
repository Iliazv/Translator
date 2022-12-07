from tkinter.tix import Select
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .utils import Translate, handle_file
from .forms import UploadFile
from vega.models import Document, HistoryObject, SelectObject, Report
import sys


def main_frame(request, signal1=0, signal2=0, arg1='none', arg2='none'):
    if arg1 == arg2 != 'none' and signal1 == 0:
        arg1 = 'none'
    elif arg1 == arg2 != 'none' and signal1 == 1:
        arg2 = 'none'
    text = request.POST.get('input_text')
    ready_text = ''
    if text != None:
        return HttpResponse(text)
        ready_text = text
    objects = HistoryObject.objects.all()[::-1]
    selected = SelectObject.objects.all()[::-1]
    favorite_condition = False

    content = {'arg1': arg1, 'arg2': arg2, 'ready_text': ready_text, 'objects': objects, 'selected': selected, 
               'favorite_condition': favorite_condition}
    template = loader.get_template('vega/main_frame.html')
    return HttpResponse(template.render(content, request))

def switch_text(request, arg1='none', arg2='none'):
    reserve_arg = arg1
    arg1 = arg2
    arg2 = reserve_arg
    text = request.POST.get('input_text')
    ready_text = ''
    if text != None:
        ready_text = text
    objects = HistoryObject.objects.all()[::-1]
    selected = SelectObject.objects.all()[::-1]

    content = {'arg1': arg1, 'arg2': arg2, 'ready_text': ready_text, 'objects': objects, 'selected': selected}
    template = loader.get_template('vega/main_frame.html')
    return HttpResponse(template.render(content, request))

def switch_file(request, arg1='none', arg2='none'):
    form = UploadFile()
    reserve_arg = arg1
    arg1 = arg2
    arg2 = reserve_arg
    text = request.POST.get('input_text')
    ready_text = ''
    if text != None:
        ready_text = text
    objects = HistoryObject.objects.all()[::-1]
    selected = SelectObject.objects.all()[::-1]

    content = {'arg1': arg1, 'arg2': arg2, 'ready_text': ready_text, 'objects': objects, 'selected': selected, 'form': form}
    template = loader.get_template('vega/documents.html')
    return HttpResponse(template.render(content, request))

def documents(request, arg1='none', arg2='none', signal1=0, signal2=0):
    form = UploadFile()
    objects = HistoryObject.objects.all()[::-1]
    selected = SelectObject.objects.all()[::-1]

    content = {'arg1': arg1, 'arg2': arg2, 'signal1': 0, 'signal2': 0, 'form': form, 'objects': objects, 'selected': selected}
    template = loader.get_template('vega/documents.html')
    return HttpResponse(template.render(content, request))

def about(request):
    content = {}
    template = loader.get_template('vega/about.html')
    return HttpResponse(template.render(content, request))

def translate(request, signal1=0, signal2=0, arg1='none', arg2='none'):
    input_text = request.POST.get('input_text')
    function = Translate(input_text, arg1, arg2)
    translation_text = input_text
    translated_text = function
    history_object = HistoryObject.objects.create(to_language=arg2, from_language=arg1, text=translation_text, 
    translate=translated_text)
    history_object.save()
    objects = HistoryObject.objects.all()[::-1]
    selected = SelectObject.objects.all()[::-1]
    favorite_condition = True

    content = {'translation_text': translation_text, 'translated_text': translated_text, 'arg1': arg1, 
               'arg2': arg2, 'objects': objects, 'selected': selected, 'favorite_condition': favorite_condition}
    template = loader.get_template('vega/main_frame.html')
    return HttpResponse(template.render(content, request))

def add_favorite(request, input='none', output='none', arg1='none', arg2='none', signal1=0, signal2=0):
    favorite = SelectObject.objects.create(to_language=arg2, from_language=arg1, text=input, 
    translate=output)
    objects = HistoryObject.objects.all()
    value = 'none'
    content = {}
    template = loader.get_template('vega/about.html')
    return redirect(reverse('main_frame', args=[arg1, arg2, signal1, signal2]))

def remove_favorite(request, id, input='none', output='none', arg1='none', arg2='none', signal1=0, signal2=0):
    favorite = SelectObject.objects.get(id=id)
    favorite.delete()
    objects = HistoryObject.objects.all()
    value = 'none'
    content = {}
    template = loader.get_template('vega/about.html')
    return redirect(reverse('main_frame', args=[arg1, arg2, signal1, signal2]))

#def remove_favorite(request, id, input='none', output='none', arg1='none', arg2='none', signal1=0, signal2=0):
#    favorite = SelectObject.objects.get(id=12)
#   favorite.delete()
 #   
 #   objects = HistoryObject.objects.all()
 #   content = {}
  #  template = loader.get_template('vega/about.html')
  #  return redirect(reverse('main_frame', args=[arg1, arg2, signal1, signal2]))

def clear_history(request, input='none', output='none', arg1='none', arg2='none', signal1=0, signal2=0):
    HistoryObject.objects.all().delete()
    content = {}
    template = loader.get_template('vega/about.html')
    return redirect(reverse('main_frame', args=[arg1, arg2, signal1, signal2]))

def clear_selected(request, input='none', output='none', arg1='none', arg2='none', signal1=0, signal2=0):
    SelectObject.objects.all().delete()
    content = {}
    template = loader.get_template('vega/about.html')
    return redirect(reverse('main_frame', args=[arg1, arg2, signal1, signal2]))

def show(request, input='none', output='none', arg1='none', arg2='none', signal1=0, signal2=0):
    objects = HistoryObject.objects.all()[::-1]
    selected = SelectObject.objects.all()[::-1]

    content = {'input': input, 'output': output, 'arg1': arg1, 
               'arg2': arg2, 'objects': objects, 'selected': selected}
    template = loader.get_template('vega/show_history.html')
    return HttpResponse(template.render(content, request))

def hello(request):
    content = {}
    template = loader.get_template('vega/main_frame.html')
    return HttpResponse()

def send_report(request):
    arg1, arg2 = 'none', 'none'
    signal1, signal2 = 0, 0
    report_text = request.POST.get('modal_input')
    report = Report.objects.create(text=report_text)
    report.save()
    objects = HistoryObject.objects.all()[::-1]
    selected = SelectObject.objects.all()[::-1]

    content = {}
    template = loader.get_template('vega/main_frame.html')
    return redirect(reverse('main_frame', args=[arg1, arg2, signal1, signal2]))

def read_file(request, arg1='none', arg2='none', signal1=0, signal2=0): 
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            text = handle_file(request.FILES['file'])
            translated_text = Translate(text, arg1, arg2)
            translation_text = text
            objects = HistoryObject.objects.all()[::-1]
            selected = SelectObject.objects.all()[::-1]

            favorite_condition, input = True, 'none'
            form.save()
    content = {'translated_text': translated_text, 'translation_text': translation_text ,'favorite_condition': favorite_condition,
               'arg1': arg1, 'arg2': arg2, 'signal1': 0, 'signal2': 0, 'form': form, 'objects': objects, 'input': input, 'selected': selected}
    template = loader.get_template('vega/documents.html')
    return HttpResponse(template.render(content, request))