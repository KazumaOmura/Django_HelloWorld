from django.shortcuts import render

#追加
def helloworldfunction(request):
    return render(request, 'index.html')