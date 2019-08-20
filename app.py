from japronto import Application
from nltkpiidetector.piidetector import PiiDetector
import json


async def nltk(request):
        req_json = request.json
        json_str = json.dumps(req_json)
        entitiesE = PiiDetector().getEntites(json_str)
        entitiesR = PiiDetector().getpatterns(json_str)
        return request.Response(json=entitiesE + entitiesR)


app = Application()

router = app.router
router.add_route('/nltk', nltk, method='POST')

app.run()

