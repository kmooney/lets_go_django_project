from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.text import slugify
from django.template import loader, RequestContext
from django.forms import ModelForm

from . models import List, Thing


# Create your views here.
class ListModelForm(ModelForm):
    class Meta: 
        model = List
        fields = ['name']

class ThingModelForm(ModelForm):
     class Meta:
         model = Thing
         fields = ['name', 'done']

def view_lists(request):
    
    lists = List.objects.all() 
    template = loader.get_template('lister/index.html')
    form = ListModelForm()
    return HttpResponse(
    	template.render(RequestContext(request, {'my_lists': lists, 'form': form}))
    )

def view_list(request, list_slug):
    things = List.objects.get(slug=list_slug).thing_set.all()
    template = loader.get_template('lister/view_list.html')
    form = ThingModelForm()
    return HttpResponse(
        template.render(RequestContext(request, {'list_slug': list_slug, 'form': form, 'things': things}))
    )

def add_new_list(request):
   # add the list, then redirect to the list of lists
   f = ListModelForm(request.POST)
   if f.is_valid():
       l = f.save(commit=False) 
       l.slug = slugify(l.name)
       l.save()
   return HttpResponseRedirect('/')
    
def add_new_thing(request, list_slug):
    f = ThingModelForm(request.POST)
    if f.is_valid():
        t = f.save(commit=False)
        t.slug = slugify(t.name)
        t.my_list = List.objects.get(slug=list_slug)
        t.save()
    return HttpResponseRedirect('/%s' % list_slug)
