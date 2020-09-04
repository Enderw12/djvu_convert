from flask import Flask, send_file, request
from werkzeug.utils import secure_filename
from converter import convert

app = Flask(__name__)


@app.route('/convert', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        inputFile = request.files['file']
        inputFileName = 'input.djvu'
        print(inputFileName)
        inputFile.save(secure_filename(inputFileName))
        outputFileName = 'output.pdf'
        path = convert(inputFileName, outputFileName)
        print(outputFileName)
        return send_file(path, as_attachment=True)
    
    if request.method == 'GET':

        return send_file('output.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
