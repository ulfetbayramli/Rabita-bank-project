import json
from flask import redirect, render_template
from flask import request
from sqlalchemy import null
from app import app
# from forms import MyForm
from forms import Online_queue
from models import Branchs, Services, Queue , Cards
from models import Cards
from models import  Queue
from models import News 
from converter import USD , EUR , GBP

    




@app.route("/emanetler", methods = ['GET','POST'])
def emanetler():
    # cards = Cards.query.all()
    return render_template('emanetler.html')

@app.route("/emanetler_etrafli", methods = ['GET','POST'])
def emanetler_etrafli():
    return render_template('emanetler_erafli.html')

@app.route("/kart_sifarisi", methods = ['GET','POST'])
def kart_sifarisi():
    return render_template('kart-sifarisi.html')

@app.route("/kampaniyalar", methods = ['GET','POST'])
def kampaniyalar():
    return render_template('kampaniyalar.html')




# from forms import ContactForm, RegisterForm , LoginForm


@app.route('/news/<int:id>')
def News_full(id):
    news = News.query.filter_by(id = id).first_or_404()
    # print(news)
    news_title = news.title
    image_status = news.image_status
    news_desc = news.text.split("\n")
    news_foot = News.query.filter_by(category=news.category)
    i=0
    for news in news_foot:
        i += 1
    return render_template('news.html', news_title = news_title, news=news, image_status = image_status, news_desc = news_desc, news_foot = news_foot, i = i)


@app.route('/news')
def News_all():
    news_all = News.query.all()
    length = len(news_all)
    i = -1
    return render_template('news_list/all.html', news_all = news_all , length = length , i = i)



@app.route('/news/<category>')
def News_category(category):
    news = News.query.filter_by(category=f"{category}")
    return render_template(f'news_list/{category}.html', news = news)






@app.route('/', methods = ['GET', 'POST'])
def Main(): 
    usd = round(USD[0], 4)
    eur = round(EUR[0], 4)
    gbp = round(GBP[0], 4)
    date = USD[1] 
    news_foot = News.query.all()
    # print(gbp)
    return render_template('home.html', usd=usd, eur=eur, gbp=gbp, date=date, news_foot = news_foot)




@app.route('/queue', methods = ['GET', 'POST'])
def Online_queu(): 
    form = Online_queue()
    form.filial.choices = [( branch.name ,branch.name) for branch in  Branchs.query.all()]
    form.xidmet.choices = [( service.name ,service.name) for service in  Services.query.all()]
    if request.method == 'POST':
        post_data = request.form
        form = Online_queue(data=post_data)
        # if form.validate_on_submit():
        print('success')
        queue = Queue(filial=form.filial.data, xidmet=form.xidmet.data, date=form.date.data ,number= form.number.data)
        queue.save()
        return redirect('/queue')
    return render_template('online_queue.html', form = form)
