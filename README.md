# Study APP
Study App Sanic API (Assync)

  ___  ___  _ __ (_) ___  | |_| |__   ___  | |__   ___  __| | __ _  ___| |__   ___   __ _ 
 / __|/ _ \| '_ \| |/ __| | __| '_ \ / _ \ | '_ \ / _ \/ _` |/ _` |/ _ \ '_ \ / _ \ / _` |
 \__ \ (_) | | | | | (__  | |_| | | |  __/ | | | |  __/ (_| | (_| |  __/ | | | (_) | (_| |
 |___/\___/|_| |_|_|\___|  \__|_| |_|\___| |_| |_|\___|\__,_|\__, |\___|_| |_|\___/ \__, |
                                                             |___/                  |___/ 

## Build With

* [Python 3.7>](https://docs.python.org/3/library/asyncio.html) - Especially the assync library from Python 3
* [Sanic](https://sanic.readthedocs.io/en/latest/) - Sanic assync python web framework
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