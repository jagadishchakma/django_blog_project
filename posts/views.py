from django.shortcuts import render, redirect

from posts.models import Post
from . import forms 

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
        return render(request, 'add_post.html', {'form': post_form})
    

#edit post
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('edit_post',id=post.id)
   
    return render(request, 'add_post.html', {'form': post_form})


#delete post
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("homepage")
