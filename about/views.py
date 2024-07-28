from django.shortcuts import render


def about(request):
    return render(request, 'about/about.html')


def privacy(request):
    return render(request, 'about/privacy-policy.html')

def purchaseGuide(request):
    return render(request, 'about/purchase-guide.html')

def terms(request):
    return render(request, 'about/terms.html')