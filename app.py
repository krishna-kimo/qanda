import pandas as pd
import json
import ktrain
from flask import Flask, jsonify, request
from settings.py import BIO_BERT_SQUAD_ML BIO_MODEL INDEXDIR

#BIO_BERT_SQUAD_ML = "ktrapeznikov/biobert_v1.1_pubmed_squad_v2"
#BIO_MODEL = 'mrm8488/GPT-2-finetuned-covid-bio-medrxiv'


#app
app = Flask(__name__)a
#qa = text.SimpleQA(index_dir=INDEXDIR,bert_squad_model=bio_bert_model, pt_value=True)


#routes
@app.route('/hello')
def greet_hello():
    return ("Hello there I am working!!!")

@app.route('/answer', methods=['POST'])
def get_answer():
    #get_data
    data = request.get_json(force=True)

    answers = qa.ask(data['q'])

    return answers

if __name__ == '__main__':
    app.run(host = ‘0.0.0.0’, port = 8080, threaded=True)
