from django.shortcuts import render
from django.views import View
from movies.forms import MovieSearchForm
from tivix_task.local_settings import omdb_api
import json

class Home(View):
    def get(self,request):
        ctx = {}

        return render(request,'home.html', ctx)

class Search(View):
    def get(self,request):
        form = MovieSearchForm()
        return render(request, 'search-engine.html', {'form':form})

    def post(self,request):
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']

            url = "{}&t={}&y={}".format(omdb_api, title, year)
            response = request.GET.get(url)
            data = json.loads(response)

        return render(request,'search-engine.html', {'data':data})
