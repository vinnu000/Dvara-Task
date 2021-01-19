from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell

from apps import app, db, models

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="127.0.0.1", port=8000))


from apps import views as view_blueprint
# app.register_blueprint(view_blueprint)


if __name__ == "__main__":
    manager.run()
