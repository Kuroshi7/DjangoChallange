import csv
import os
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def read_csv():
    file_path = os.path.join(os.path.dirname(__file__), '../alunos.csv')
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def csv_viewer(request):
    data = read_csv()
    return render(request, 'csv_viewer.html', {'data': data})

def image_viewer(request):
    image_url = ''
    if request.method == 'POST':
        image_url = request.POST.get('image_url', '')  # Obtém a URL inserida no campo 
    return render(request, 'image_viewer.html', {'image_url': image_url})