import json
from watson_developer_cloud import ToneAnalyzerV3
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

# You must create your own plotly account for this to work - register here:
# https://plot.ly/accounts/login/?next=%2Fsettings%2Fapi
# after you create account, go here: 
# http://plot.ly/settings/api
# copy your username, paste it below!
# generate a new API key, paste it below!
plotly.tools.set_credentials_file(username='YOUR USERNAME HERE', api_key='YOUR API KEY')

tone_analyzer = ToneAnalyzerV3(
   username='4c3ca360-5df4-48d2-8a15-9546c7b08454',
   password='dYKqK7TtSwTz',
   version='2016-05-19 ')

sentimentJSON = tone_analyzer.tone(text='Wow, GOD DAMN! I am SO CONFIDENT!')['document_tone']['tone_categories']

# emotional tones
anger = sentimentJSON[0]["tones"][0]["score"];
disgust = sentimentJSON[0]["tones"][1]["score"];
fear = sentimentJSON[0]["tones"][2]["score"];
joy = sentimentJSON[0]["tones"][3]["score"];
sadness = sentimentJSON[0]["tones"][4]["score"];

# language tone
analytical = sentimentJSON[1]["tones"][0]["score"];
confident = sentimentJSON[1]["tones"][1]["score"];
tentative = sentimentJSON[1]["tones"][2]["score"];

# social tones
openness = sentimentJSON[2]["tones"][0]["score"];
conscientiousness = sentimentJSON[2]["tones"][1]["score"];
extraversion = sentimentJSON[2]["tones"][2]["score"];
agreeableness = sentimentJSON[2]["tones"][3]["score"];
emotionalRange = sentimentJSON[2]["tones"][4]["score"];

data = [go.Bar(
            x=[
                'anger', 'disgust', 'fear', 'joy', 'sadness', 
                'analytical', 'confident', 'tentative', 
                'openness', 'conscientiousness', 'extraversion', 'agreeableness', 'emotional range'],
            y=[
                anger, disgust, fear, joy, sadness,
                analytical, confident, tentative,
                openness, conscientiousness, extraversion, agreeableness, emotionalRange]
        )]

py.plot(data, filename='basic-bar')
