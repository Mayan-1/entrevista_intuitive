from os import listdir
from bs4 import BeautifulSoup
import requests
import  os
from  zipfile import ZipFile


def baixar_arquivos(content):
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find("ol").find_all("a")

    i = 0

    for link in links:
        if '.pdf' in link.get('href', []):
            i += 1
            print("Baixando arquivo: ", i)

            response = requests.get(link.get('href'))

            pdf = open("pdf" + str(i) + ".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("Arquivo ", i, " baixado")


def compactar_arquivos(path):
    with ZipFile(path+"/arquivo_comp.zip", "w") as zip:
        for i in listdir():
            if i.endswith(".pdf"):
                zip.write(i)
                os.remove(i)


if __name__ == '__main__':
    path = r'C:\entrevista_intuitive\web_scraping'
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
    content = requests.get(url, headers).content

    baixar_arquivos(content)
    compactar_arquivos(path)
    print("Todos os arquivos foram baixados")







