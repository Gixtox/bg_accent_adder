import unicodedata
import wikipediaapi
import json

# This is a temporary file I used for creating the custom accented characters and for creating the initial dictionary.

# https://en.wikipedia.org/wiki/Cyrillic_script_in_Unicode#Basic_Cyrillic_alphabet

# а̀ ѐ ѝ о̀ у̀  я̀ 

def main():
    accented = {
        '\u0410':unicodedata.normalize('NFC','\u0410\u0301'), # 'А': 'А́', 
        '\u0415':unicodedata.normalize('NFC','\u0415\u0301'), # 'Е': 'Е́', 
        '\u0418':unicodedata.normalize('NFC','\u0418\u0301'), # 'И': 'И́', 
        '\u0419':unicodedata.normalize('NFC','\u0419\u0301'), # 'Й': 'Й́', 
        '\u041E':unicodedata.normalize('NFC','\u041E\u0301'), # 'О': 'О́', 
        '\u0423':unicodedata.normalize('NFC','\u0423\u0301'), # 'У': 'У́', 
        '\u042A':unicodedata.normalize('NFC','\u042A\u0301'), # 'Ъ': 'Ъ́', 
        '\u042E':unicodedata.normalize('NFC','\u042E\u0301'), # 'Ю': 'Ю́', 
        '\u042F':unicodedata.normalize('NFC','\u042F\u0301'), # 'Я': 'Я́', 
        '\u0430':unicodedata.normalize('NFC','\u0430\u0301'), # 'а': 'а́', 
        '\u0435':unicodedata.normalize('NFC','\u0435\u0301'), # 'е': 'е́', 
        '\u0438':unicodedata.normalize('NFC','\u0438\u0301'), # 'и': 'и́', 
        '\u0439':unicodedata.normalize('NFC','\u0439\u0301'), # 'й': 'й́', 
        '\u043E':unicodedata.normalize('NFC','\u043E\u0301'), # 'о': 'о́', 
        '\u0443':unicodedata.normalize('NFC','\u0443\u0301'), # 'у': 'у́', 
        '\u044A':unicodedata.normalize('NFC','\u044A\u0301'), # 'ъ': 'ъ́', 
        '\u044E':unicodedata.normalize('NFC','\u044E\u0301'), # 'ю': 'ю́', 
        '\u044F':unicodedata.normalize('NFC','\u044F\u0301'), # 'я': 'я́' 
        }

    a = []
    with open('dictionary.json', 'r') as file:
        a = file.readlines()
    print(a[63])
    a = {f'{x.strip()}':x.strip() for x in a}

    with open('dictionary2.json', 'w') as file:
         file.write(str(json.dumps(a, ensure_ascii=False)))
    # print(a)

if __name__ == '__main__':
    main()