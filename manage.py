from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Stories
from  flask_migrate import Migrate, MigrateCommand

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

# app = create_app('development')


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

#this decorator allows us to pass properties into my shell
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User=User,Stories = Stories )

if __name__ == '__main__':
    manager.run()
