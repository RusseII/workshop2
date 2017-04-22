import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
   username='4c3ca360-5df4-48d2-8a15-9546c7b08454',
   password='dYKqK7TtSwTz',
   version='2016-05-19 ')

print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))
