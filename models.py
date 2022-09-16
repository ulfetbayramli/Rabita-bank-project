from pydoc import describe
from app import app
from extensions import db 

# from app import app
# from datetime import datetime 





 



class Cards(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text(), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    # icon isval subcard

    # def _repr_(self):
    #     return f'{self.title}, {self.description}, {self.image}'

    def _init_(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image

    def save(self):
        db.session.add(self)
        db.session.commit()



class News(db.Model):
    id = db.Column(db.Integer ,primary_key = True)
    category= db.Column(db.String(50))
    title = db.Column(db.String(255))
    text = db.Column(db.Text )
    image_status = db.Column (db.Boolean)
    image = db.Column(db.Text )
    added_at = db.Column(db.Date, default=db.func.now())

    def __repr__(self):
        return self.title

    def __init__(self, category, title, text,image_status , image, added_at):
        self.category = category
        self.title = title
        self.text = text
        self.image_status = image_status
        self.image = image
        self.added_at = added_at

    def save(self):
        db.session.add(self)
        db.session.commit()


class Queue(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filial = db.Column(db.String(50) , nullable=False)
    xidmet = db.Column(db.String(50) , nullable=False)
    date=db.Column(db.Date(),nullable=True)
    number = db.Column(db.Integer() , nullable=False)

    def __init__(self , filial, xidmet, date, number):
        self.filial = filial
        self.xidmet = xidmet
        self.date = date
        self.number = number

    def save(self):
        db.session.add(self)
        db.session.commit()


class Branchs(db.Model):
    id = db.Column(db.Integer ,primary_key = True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name
        
    def save(self):
        db.session.add(self)
        db.session.commit()


class Services(db.Model):
    id = db.Column(db.Integer ,primary_key = True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name
        
    def save(self):
        db.session.add(self)
        db.session.commit()

