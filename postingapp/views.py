from django.shortcuts import render

# Create your views here.
def postings(request):
    return render(request, 'postings.html')

def write(request):
    return render(request, 'write.html')