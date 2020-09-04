from flask import Flask, send_file, request
from werkzeug.utils import secure_filename
from converter import convert

# это простейший веб-сервер на основе фреймворка flask.
# Обрабатывает лишь один адрес и два типа запросов. 

app = Flask(__name__)


@app.route('/convert', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        # при методе запроса POST "достаём" из запроса файл djvu
        inputFile = request.files['file']
        # присваиваем имя для хранения в папке сервера
        inputFileName = 'input.djvu'
        print(inputFileName) # печатаем в консоль, что не совсем правильно, зто очень удобно, учитывая тип выполняемой задачи не вредит. 
        inputFile.save(secure_filename(inputFileName)) # сохраняем файл в папке сервера
        outputFileName = 'output.pdf'
        path = convert(inputFileName, outputFileName) # вызов функции из импортированного модуля который конвертирует полученный документ и возвращает имя pdf документа
        print(outputFileName)
        return send_file(path, as_attachment=True) # возвращаем ответ с pdf документом
    
    if request.method == 'GET':
        # позволяет получить последний конвертированный документ простым переходом по ссылке из браузера. Но здесь мог бы быть и другой, более полезный код.
        return send_file('output.pdf', as_attachment=True)

# если запущен этот модуль, то исполнить метод run объекта Flask (запускаем вебсервер)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
