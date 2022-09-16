from flask import Flask

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)
API_KEY = '4HX3N1FOEYU6RAYC'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@127.0.0.1:3306/rabita_bank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config ['SECRET_KEY'] = 'my_project'

from controllers import *
from extensions import * 
from models import * 


if __name__ == '__main__':
    app.init_app(db)
    app.init_app(migrate)
    app.run(port=5000, debug=True)


admin = Admin(app)

admin.add_view(ModelView(News, db.session))
admin.add_view(ModelView(Queue, db.session))
admin.add_view(ModelView(Branchs, db.session))
admin.add_view(ModelView(Services, db.session))



admin.add_view(ModelView(Cards, db.session))
