import subprocess
# subprocess позволяет обращаться к системным библиотекам на языке shell скриптов

def convert(inputFileName, outputFileName):
    # обращаемся к библиотеке ddjvu которая умеет конвертировать djvu в pdf 
    # качество изображений на 60% из возможных 140%
    # передаём имя (оно же путь к файлу который нужно конвертировать)
    result = subprocess.run(
        ['ddjvu', '-quality=60', '-format=pdf', inputFileName, outputFileName, ])
    # возвращаем имя файла по завершению конвертации (оно же и путь, ибо файл находится в той же папке что и программа)
    return result.args[-1]
