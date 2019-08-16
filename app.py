from vibora import Vibora, Request
from vibora.responses import JsonResponse
from nltkpiidetector.piidetector import PiiDetector
import json

app = Vibora()

@app.route('/nltk_ner',methods=['POST'])
async def spacy_ner(request: Request):
        json = await request.json()
        json_str = json.dump(json)
        entities = PiiDetector().getEntites(json_str)
        return JsonResponse(entities)

@app.route('/nltk_regex',methods=['POST'])
async def spacy_ner(request: Request):
        json = await request.json()
        json_str = json.dump(json)
        entities = PiiDetector().getpatterns(json_str)
        return JsonResponse(entities)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)

