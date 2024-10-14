from django.shortcuts import render
def load_data_view(request):
    # Apenas um exemplo de função de visualização
    return render(request, 'data_loader/data_view.html')

def sample_view(request):
    return HttpResponse("Esta é uma página de exemplo.")