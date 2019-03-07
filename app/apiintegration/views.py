from django.shortcuts import render
from django.views import View
import requests
# Create your views here.

class Post(View):
    def get(self,request):
        r = requests.get('http://jsonplaceholder.typicode.com/posts')
        if r.status_code == requests.codes.ok:
            context={ 'posts' : r.json()}
        else:
            context={ 'posts' : []}
        return render(request, 'apiintegration/index.html',context)


class PostComments(View):
    def get(self,request,slug):
        r = requests.get('http://jsonplaceholder.typicode.com/comments/?postId=' + slug )
        if r.status_code == requests.codes.ok:
            comments=r.json()
        else:
            comments=[]

        r1 = requests.get('http://jsonplaceholder.typicode.com/posts/?id=' + slug )
        if r1.status_code == requests.codes.ok:
            post=r1.json()[0]
        else:
            post= {}

        return render(request, 'apiintegration/comments.html',context = { 'comments':comments, 'post':post})