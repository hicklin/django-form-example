from django.shortcuts import get_object_or_404, render

def render_form(request):
    return render(request, 'formone.html')

def result_page(request, some_id):
    test_text = request.POST.get('testtext')
    return render(request, 'success.html', {'test_text': test_text, 'some_id': some_id})
