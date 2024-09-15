# Projeto Django WebHub

Este é um projeto Django simples para gerenciar uma aplicação web com páginas para exibir imagens e dados de um arquivo CSV. O projeto inclui as seguintes páginas:

- **Home Page**: Página inicial com links para visualizar imagens e dados CSV.
- **Image Viewer**: Página para exibir uma imagem a partir de uma URL.
- **CSV Viewer**: Página para exibir dados de um arquivo CSV.

  Certifique-se de ter o Python e o pip instalados. Além disso, é necessário o Django e outros pacotes listados no `requirements.txt`.
**Clone o repositório**:

    ```bash
    git clone https://github.com/Kuroshi7/DjangoChallange.git
    ```
**Instale as dependências**:
va ate o diretorio WebHub
   ```bash
    pip install -r requirements.txt
   ```

## Executando o Projeto

Para iniciar o servidor de desenvolvimento do Django, execute no diretorio do manage.py:

  ```bash
   python manage.py runserver
  ```
## Utilizando as paginas
- A primeira pagina serve como um redirecionamento paras as maginas Image e CSV viewer
- A pagina de image Viewer coloque um URL valido de uma imagem na web e ela sera mostrada abaixo na tela
- CSV viwer mostra uma tabela de alunos contendo nome, idade, peso e altura respectivamente
