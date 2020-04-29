import pandas as pd
import os
import json
import ktrain
from ktrain import text
from operator import itemgetter
from flask import Flask, jsonify, request, Response
from settings import BIO_BERT_SQUAD_ML, BIO_MODEL, INDEXDIR

#BIO_BERT_SQUAD_ML = "ktrapeznikov/biobert_v1.1_pubmed_squad_v2"
#BIO_MODEL = 'mrm8488/GPT-2-finetuned-covid-bio-medrxiv'


#app
app = Flask(__name__)
qa = text.SimpleQA(index_dir=INDEXDIR, \
        bert_squad_model=BIO_BERT_SQUAD_ML, \
        bert_emb_model= BIO_MODEL, \
        from_pytorch=True)

#Util Functions
def create_json(_answers):
    # create a json array for the answers list
    #sort the list by the confidence score
    #_response = answers.sort(key=itemgetter('confidence'))
    answers = []
    for item in _answers:
        new_item = {}
        new_item['confidence'] = float(item['confidence'])
        new_item['answer'] = item['full_answer']
        new_item['context'] = item['context']
        new_item['similarity_score'] = float(item['similarity_score'])
        new_item['reference'] = int(item['reference']) ### Need to fetch relevant doc from MongoDB
        answers.append(new_item)
    return json.dumps(answers)


#routes
@app.route('/hello')
def greet_hello():
    return ("Hello there I am working!!!")

@app.route('/answer', methods=['POST'])
def get_answer():
    #get_data
    data = request.get_json(force=True)

    answers = qa.ask(data['q'])

    _response = create_json(answers)
    
    #print(_response)

    return Response(_response,  mimetype='application/json')

if __name__ == '__main__':
    #app.run(host = "0.0.0.0", port = 8080, threaded=True)
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
