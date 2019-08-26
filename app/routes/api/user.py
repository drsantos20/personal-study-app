from sanic.response import json
from sanic.response import text

from app.model.user import users

def setup_routes(app):
    @app.route("/")
    async def index(request):
        return json({"hello": "world"})

    @app.route("/users", methods=["POST",])
    async def create_user(request):
        ins = users.insert().values(name='jack', email='jack@gmail.com')
        await request.app.db.execute(ins)
        return text("You are trying to create a user with the following POST: %s" % request.body)