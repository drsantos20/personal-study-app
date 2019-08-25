from sanic.response import json

def setup_routes(app):
    @app.route("/")
    async def index(request):
        print('daniel')
        return json({"hello": "world"})
