
# Create your views here.
from django.shortcuts import render 
from .forms import EstudianteForm, ProfesorForm, CursoForm, CamadaForm

def home(request):
    return render(request, "entrega/home.html") 

def Curso(request):
    return render(request, "entrega/curso.html") 

def index(request):
    return render(request, 'index.html')

def estudiante_form(request):
    form = EstudianteForm()
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'estudiante_form.html', {'form': form})

def profesor_form(request):
    form = ProfesorForm()
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'profesor_form.html', {'form': form})

def curso_form(request):
    form = CursoForm()
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'curso_form.html', {'form': form})

def camada_search(request):
    form = CamadaForm()
    if request.method == 'POST':
        form = CamadaForm(request.POST)
        if form.is_valid():
            camada = form.cleaned_data['camada']
            cursos = Curso.objects.filter(camada=camada)
            return render(request, 'camada_search_results.html', {'cursos': cursos})
    return render(request, 'camada_search.html', {'form': form})