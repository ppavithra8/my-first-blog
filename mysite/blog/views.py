from django.shortcuts import render

# Create your views 
def post_list(request):
    return render(request, 'blog/post_list.html', {})

