import requests

userdata = { 'time': 1.5,
             'times':5400, 
             'ta':15.61, 
             'rs':0.0, 
             'tin_windavg':20, 
             'tin_dooravg':19.7, 
             'setpoint':17}

r = requests.post('http://ojasvisharma.pythonanywhere.com/predict',  data=userdata)

s = r.content.decode('ASCII', 'ignore')

print('\nresult: ', s.split("\"")[3])