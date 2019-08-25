from sanic.response import json

def setup_routes(app):
    @app.route("/")
    async def index(request):
        return json({"hello": "world"})