from flask import Flask, render_template, request
from encode import brain
from decode import brain1
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choice_decode')
def decoding():
    return render_template('decode.html')


@app.route('/decoding_process', methods=['POST', 'GET'])
def decoding_process():
    if request.method == 'POST':
        form_data = request.form
        word_input = form_data['input_name']

        strr = brain1(word_input)

        name_input = "abeer"
        cipher_text, matrix = brain(name_input)
        matrix1 = matrix[0]
        matrix2 = matrix[1]
        matrix3 = matrix[2]
        matrix4 = matrix[3]
        matrix5 = matrix[4]
        return render_template('decode_procedure.html', cypher_output=strr, matrix_output_1=matrix1,
                               matrix_output_2=matrix2, matrix_output_3=matrix3, matrix_output_4=matrix4,
                               matrix_output_5=matrix5)


@app.route('/choice_encode', methods=['POST', 'GET'])
def encoding():
    return render_template('encode.html')


@app.route("/encode_process", methods=['POST', 'GET'])
def encoding_process():
    if request.method == 'POST':
        form_data = request.form

        name_input = form_data['input_name']
        cipher_text, matrix = brain(name_input)
        matrix1 = matrix[0]
        matrix2 = matrix[1]
        matrix3 = matrix[2]
        matrix4 = matrix[3]
        matrix5 = matrix[4]

        return render_template('encode_procedure.html', cypher_output=cipher_text, matrix_output_1=matrix1,
                               matrix_output_2=matrix2, matrix_output_3=matrix3, matrix_output_4=matrix4,
                               matrix_output_5=matrix5
                               , input_name=name_input)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
