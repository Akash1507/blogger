from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect


from .forms import PostModelForm
from .models import Post

@staff_member_required
def createPost(request):
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = PostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)

@staff_member_required
def updatePost(request, postUrl):
    obj = get_object_or_404(Post, postUrl=postUrl)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": f"Update {obj.postTitle}", "form": form}
    return render(request, template_name, context)


@staff_member_required
def deletePost(request, postUrl):
    obj = get_object_or_404(Post, postUrl=postUrl)
    template_name = 'delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"object": obj}
    return render(request, template_name, context)


def listPost(request):
    postObjects = Post.objects.all().published()
    if request.user.is_authenticated:
        data = Post.objects.all()
        postData = (postObjects | data).distinct()
    template_name = 'list.html'
    context = {'objectList': postData}
    return render(request, template_name, context)


def detailPost(request, postUrl):
    obj = get_object_or_404(Post, postUrl=postUrl)
    template_name = 'detail.html'
    context = {"object": obj,"detail":True}
    return render(request, template_name, context)