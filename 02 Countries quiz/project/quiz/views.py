from django.shortcuts import render

# Create your views here.
def home(request):
    template = "home.html"
    return render(request, template)


def main(request):
    template = "quiz/main.html"
    return render(request, template)
