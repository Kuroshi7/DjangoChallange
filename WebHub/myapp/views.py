import csv
import os
from django.shortcuts import render

def index(request):
    return render(request, 'index.html') #renderiza pagina principal

def read_csv():
    file_path = os.path.join(os.path.dirname(__file__), '../alunos.csv') #retorna diretorio em que o arquivo esta juntando cmainhos cirando um caminho completo
    data = [] #lista vazia para armazenar CSV
    with open(file_path, mode='r') as file: 
        reader = csv.DictReader(file) #converte em dicionario
        for row in reader: #itera sobre cada linha no arquivo
            data.append(row) #para linha lida adiciona ao dicio nario "linha" a lista data.
    return data #retorna lista "data" que contem linhas do arquivo como dicionarios.

def csv_viewer(request):
    data = read_csv() #chama funçao armazena dados na variavel
    return render(request, 'csv_viewer.html', {'data': data}) #envia dados lidos para template com chave "data"

def image_viewer(request):
    image_url = '' #inicia variavel
    if request.method == 'POST': #verifica metodo da requisiçao HTTP
        image_url = request.POST.get('image_url', '')  # extrai valor armazena URL em "image_url"
    return render(request, 'image_viewer.html', {'image_url': image_url})#renderiza e passa a um dicionario a URL como "image_url"