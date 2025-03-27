from os import listdir
import os
import tabula
import pandas as pd
from zipfile import ZipFile


def converter_pdf_csv(pdf_path, csv_path):
    tabula.convert_into(pdf_path, csv_path, output_format='csv', pages='all', lattice=True)


def alterar_coluna(csv_path):
    df = pd.read_csv(csv_path, encoding='utf-8', engine='python', skip_blank_lines=True, quotechar='"')
    df.columns = df.columns.str.strip().str.replace('"', '')

    df.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}, inplace=True)

    df.dropna(how='all', inplace=True)
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

def compactar_arquivo():
    with ZipFile("Teste_Mayan.zip", 'w') as zip:
        for i in listdir():
            if i.endswith(".csv"):
                zip.write(i)
                os.remove(i)



if __name__ == '__main__':
    pdf_path = "pdf1.pdf"
    csv_path = "Teste_Mayan.csv"

    converter_pdf_csv(pdf_path, csv_path)
    alterar_coluna(csv_path)
    compactar_arquivo()

    print("CSV limpo e corrigido com sucesso!")
