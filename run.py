# import os
from api import create_app
from api.model import initialize_db

if __name__ == '__main__':
    app = create_app('dev')
    app.app_context().push()
    
    initialize_db.init()

    app.run()
