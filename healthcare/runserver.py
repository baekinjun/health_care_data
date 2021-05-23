from management import create_app
from flask_script import Manager
import gevent.monkey
gevent.monkey.patch_all()
app = create_app()
manager = Manager(app)


@manager.command
def dev_run():
    app.run(debug=True, port=2000)


if __name__ == '__main__':
    manager.run()
