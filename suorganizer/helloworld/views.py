from django.shortcuts import render

# Create your views here.

from datetime import date

from organizer.models import Tag, Startup, NewsLink

from blog.models import Post

from django.http import HttpResponse

def greeting(request):

	for tag in Tag.objects.all():
		tag.delete()

	Tag.objects.create(name='new_tag', slug='theSlug')

	result = Tag.objects.all()

	one = Tag.objects.all()[0]
	one.name = 'edited_tag'
	one.save()

	return HttpResponse(result)







