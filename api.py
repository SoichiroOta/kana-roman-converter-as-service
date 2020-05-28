import os
import json

import responder
import pykakasi


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']

api = responder.API(debug=DEBUG)
kakasi = pykakasi.kakasi()
conv = kakasi.getConverter()


@api.route("/")
async def convert(req, resp):
    body = await req.text
    texts = json.loads(body)
    result = [conv.convert(text) for text in texts]
    resp.media = dict(data=result)


if __name__ == "__main__":
    api.run()