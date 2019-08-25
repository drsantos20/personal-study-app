from sanic import Sanic

from databases import Database
from environs import Env
from sanic.response import json

from app.config.dev import Settings
from app.routes.api.user import setup_routes

app = Sanic(__name__)

setup_routes(app)

def setup_database():
    app.db = Database(app.config.DB_URL)

    @app.listener('after_server_start')
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener('after_server_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()

if __name__ == "__main__":
    env = Env()
    env.read_env()

    app.config.from_object(Settings)
    setup_database()
    app.run(host="0.0.0.0", port=8000)