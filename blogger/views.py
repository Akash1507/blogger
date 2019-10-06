from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect


from .forms import PostModelForm
from .models import Post


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


def updatePost(request, postUrl):
    obj = get_object_or_404(Post, postUrl=postUrl)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": f"Update {obj.postTitle}", "form": form}
    return render(request, template_name, context)



def deletePost(request, postUrl):
    obj = get_object_or_404(Post, postUrl=postUrl)
    template_name = 'delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/")
    context = {"object": obj}
    return render(request, template_name, context)

def make_pagination_html(current_page, total_pages):
    pagination_string = ""
    if current_page > 1:
        pagination_string += '<li><a href="?page=%s">◀</a></li>' % (current_page -1)
    pagination_string += '<li><span class="current"> Page %s of %s </span></li>' %(current_page, total_pages)
    if current_page < total_pages:
        pagination_string += '<li><a href="?page=%s">▶</a></li>' % (current_page + 1)
    return pagination_string


def listPost(request):
    postObjects = Post.objects.all().published()
    if request.user.is_authenticated:
        print(request.user)
        template_name = 'list.html'
        current_page = int(request.GET.get('page', '1'))
        limit = int(5 * current_page)
        offset = limit - 5
        post_list = Post.objects.filter(postUser=request.user)[offset:limit]
        total_posts = Post.objects.all().count()
        total_pages = total_posts // 5
        if total_posts % 5 != 0:
            total_pages += 1
        pagination = make_pagination_html(current_page, total_pages)
        context = {'objectList': post_list, 'pagination': pagination}

    else:
        template_name = 'normal.html'
        context = {}
    return render(request, template_name, context)


def detailPost(request, postUrl):
    obj = get_object_or_404(Post, postUrl=postUrl)
    template_name = 'detail.html'
    context = {"object": obj,"detail":True}
    return render(request, template_name, context)