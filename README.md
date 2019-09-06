# Study APP
Study App Sanic API (Async)

## Build With

* [Python 3.7>](https://docs.python.org/3/library/asyncio.html) - Especially the async library from Python 3
* [Sanic](https://sanic.readthedocs.io/en/latest/) - Sanic async python web framework
* [SQLAlchemy Core](https://docs.sqlalchemy.org/en/13/core/) - SQLAlchemy Core
* [SQLAlchemy Migrate](https://sqlalchemy-migrate.readthedocs.io/en/latest/index.html) - SQLAlchemy Migrate (schema change management)

## SQLAlchemy Migration

 - manage.py from migrations shortcut (In the root folder type):

 Make Migrations:
 
```buildoutcfg
1 - migrate manage manage.py --repository=my_repository --url=sqlite:///project.db
2 - python migrations/manage.py version_control
3 - python manage upgrade

```
