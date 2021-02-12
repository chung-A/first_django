from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.http import HttpResponseRedirect
from second.models import Post
from second.serializers import PostSerializer
from .forms import PostForm


# Create your views here.
def select(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            newItem = form.save()

        return HttpResponseRedirect('/second/list/')

    # GET 으로 접근 시.
    form = PostForm()
    return render(request, 'second/create.html', {'form': form})


def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid():
        return render(request, 'second/confirm.html', {'form': form})
    else:
        return HttpResponseRedirect('/second/create/')


class PostRestFul(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(post=self.request.user)
