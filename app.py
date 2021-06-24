from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator

# from textblob import TextBlob

app = Flask(__name__)

person = {
    'title': '我的简历',
    'first_name': '毅文',
    'last_name': '何',
    'name': '何毅文',
    'sx': 'hyw',
    'drive': '123 My Place Drive',
    'address': 'Hogwarts · Alnwick Castle',
    'job': 'student',
    'tel': '123123123',
    'email': '123123123@yahoo.com',
    'profile': '个人简介',
    'description': '''本人性格开朗、稳重、有活力，待人热情、真诚;工作认真负责，积极主动，能吃苦耐劳，用于承受压力，勇于创新;有很强的组织能力和团队协作精神，具有较强的适
    应能力;纪律性强，工作积极配合;意志坚强，具有较强的无私奉献精神。对待工作认真负责，善于沟通、协调有较强的组织能力与团队精神;活泼开朗、乐观上进、有爱心并善于施教并行;上进心强、勤于学习能不断提高自身的能力与综合素质。''',
    'social_media': [
        {
            'link': 'https://www.facebook.com/nono',
            'icon': 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon': 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon': 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon': 'fa-twitter'
        }
    ],
    'img': 'img/imgn.jpg',
    'experiences': [
        {
            'title': 'Web Developer',
            'company': 'AZULIK',
            'description': 'Project manager and lead developer for several AZULIK websites.',
            'timeframe': 'July 2018 - November 2019'
        },
        {
            'title': 'Freelance Web Developer',
            'company': 'Independant',
            'description': 'Create Wordpress websites for small and medium companies. ',
            'timeframe': 'February 2017 - Present'
        },
        {
            'title': 'Sharepoint Intern',
            'company': 'ALTEN',
            'description': 'Help to manage a 600 Sharepoint sites platform (audit, migration to Sharepoint newer versions)',
            'timeframe': 'October 2015 - October 2016'
        }
    ],
    'education': [
        {
            'university': 'Paris Diderot',
            'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'description': 'Gestion de projets IT, Audit, Programmation',
            'mention': 'Bien',
            'timeframe': '2015 - 2016'
        },
        {
            'university': 'Paris Dauphine',
            'degree': 'Master en Management global',
            'description': 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
            'mention': 'Bien',
            'timeframe': '2015'
        },
        {
            'university': 'Lycée Turgot - Paris Sorbonne',
            'degree': 'CPGE Economie & Gestion',
            'description': 'Préparation au concours de l\'ENS Cachan, section Economie',
            'mention': 'N/A',
            'timeframe': '2010 - 2012'
        }
    ],
    'programming_languages': {
        'HMTL': ['fa-html5', '100'],
        'CSS': ['fa-css3-alt', '100'],
        'SASS': ['fa-sass', '90'],
        'JS': ['fa-js-square', '90'],
        'Wordpress': ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB': ['fa-database', '60'],
        'MySQL': ['fa-database', '60'],
        'NodeJS': ['fa-node-js', '50']
    },
    'languages': {'French': 'Native', 'English': 'Professional', 'Spanish': 'Professional',
                  'Italian': 'Limited Working Proficiency'},
    'interests': ['Dance', 'Travel', 'Languages']
}


@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)


@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm3(request.args.get('data'))


# @app.route('/chart2')
# def chart2():
#     return render_template('chartsajax1.html', graphJSON=gm2())
#
#
# def gm2(sex="MALE"):
#     df = pd.read_csv('penguins.csv')
#
#     fig = px.line(df[df['sex'] == sex], x="bill_length_mm", y="bill_depth_mm", color="island")
#
#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return graphJSON


@app.route('/chart3')
def chart3():
    return render_template('chartsajax2.html', graphJSON=gm3(), graphJSON1=gm4(), graphJSON2=gm5(),graphJSON3=gm6(),graphJSON4=gm7(),graphJSON5=gm8(),graphJSON6=gm9())


def gm3(attention="divided"):
    df = pd.read_csv('attention.csv')

    fig = px.line(df[df['attention'] == attention], x="subject", y="score", color="solutions")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def gm4(attention="divided"):
    df = pd.read_csv('attention.csv')

    fig = px.bar(df[df['attention'] == attention], x="subject", y="score", color="solutions")
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1


def gm5(attention="divided"):
    df = pd.read_csv('attention.csv')

    fig = px.scatter(df[df['attention'] == attention], x="subject", y="score", color="solutions")
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2

def gm6(attention="divided"):
    df = pd.read_csv('attention.csv')

    fig = px.area(df[df['attention'] == attention], x="subject", y="score", color="solutions")
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3

def gm7(attention="divided"):
    df = pd.read_csv('attention.csv')

    fig = px.scatter_ternary(df[df['attention'] == attention], a="subject", b="score", c="solutions", color="num")
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON4

def gm8(attention="divided"):
    df = pd.read_csv('attention.csv')

    fig = px.scatter_polar(df[df['attention'] == attention], r="subject", theta="num", color="score", symbol="solutions")
    graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5

def gm9(attention="divided"):
    df = pd.read_csv('attention.csv')

    fig = px.scatter_3d(df[df['attention'] == attention], x="subject", y="score", z="solutions", color="num")
    graphJSON6 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON6

@app.route('/chart4')
def chart4():
    return render_template('chartsajax1.html', graphJSON7=gm10(), graphJSON8=gm11(), graphJSON9=gm12(),graphJSON10=gm13(),graphJSON11=gm14(),graphJSON12=gm15(),graphJSON13=gm16())


def gm10(sex="MALE"):
    df = pd.read_csv('penguins.csv')

    fig = px.line(df[df['sex'] == sex], x="bill_length_mm", y="bill_depth_mm", color="island")
    graphJSON7 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON7


def gm11(sex="MALE"):
    df = pd.read_csv('penguins.csv')

    fig = px.bar(df[df['sex'] == sex], x="bill_length_mm", y="bill_depth_mm", color="island")
    graphJSON8 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON8


def gm12(sex="MALE"):
    df = pd.read_csv('penguins.csv')

    fig = px.scatter(df[df['sex'] == sex], x="bill_length_mm", y="bill_depth_mm", color="island")
    graphJSON9 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON9

def gm13(sex="MALE"):
    df = pd.read_csv('penguins.csv')

    fig = px.area(df[df['sex'] == sex], x="bill_length_mm", y="bill_depth_mm", color="island")
    graphJSON10 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON10

def gm14(sex="MALE"):
    df = pd.read_csv('penguins.csv')

    fig = px.scatter_ternary(df[df['sex'] == sex], a="bill_length_mm", b="bill_depth_mm", c="body_mass_g", color="flipper_length_mm")
    graphJSON11 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON11

def gm15(sex="MALE"):
    df = pd.read_csv('penguins.csv')

    fig = px.scatter_polar(df[df['sex'] == sex], r="bill_length_mm", theta="body_mass_g", color="flipper_length_mm", symbol="species")
    graphJSON12 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON12

def gm16(sex="MALE"):
    df = pd.read_csv('penguins.csv')

    fig = px.scatter_3d(df[df['sex'] == sex], x="bill_length_mm", y="bill_depth_mm", z="species", color="flipper_length_mm")
    graphJSON13 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON13


@app.route('/senti')
def main():
    text = ""
    values = {"positive": 0, "negative": 0, "neutral": 0}

    with open('ask_politics.csv', 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for idx, row in enumerate(reader):
            if idx > 0 and idx % 2000 == 0:
                break
            if 'text' in row:
                nolinkstext = re.sub(
                    r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                    '', row['text'], flags=re.MULTILINE)
                text = nolinkstext

            blob = TextBlob(text)
            for sentence in blob.sentences:
                sentiment_value = sentence.sentiment.polarity
                if sentiment_value >= -0.1 and sentiment_value <= 0.1:
                    values['neutral'] += 1
                elif sentiment_value < 0:
                    values['negative'] += 1
                elif sentiment_value > 0:
                    values['positive'] += 1

    values = sorted(values.items(), key=operator.itemgetter(1))
    top_ten = list(reversed(values))
    if len(top_ten) >= 11:
        top_ten = top_ten[1:11]
    else:
        top_ten = top_ten[0:len(top_ten)]

    top_ten_list_vals = []
    top_ten_list_labels = []
    for language in top_ten:
        top_ten_list_vals.append(language[1])
        top_ten_list_labels.append(language[0])

    graph_values = [{
        'labels': top_ten_list_labels,
        'values': top_ten_list_vals,
        'type': 'pie',
        'insidetextfont': {'color': '#FFFFFF',
                           'size': '14',
                           },
        'textfont': {'color': '#FFFFFF',
                     'size': '14',
                     },
    }]

    layout = {'title': '<b>意见挖掘</b>'}

    return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
