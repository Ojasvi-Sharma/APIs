import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def make_prediction():

	if request.method=='POST':

		time = request.form.get('time')
		times = request.form.get('times')
		ta = request.form.get('ta')
		rs = request.form.get('rs')
		tin_windavg = request.form.get('tin_windavg')
		tin_dooravg = request.form.get('tin_dooravg')
		setpoint = request.form.get('setpoint')

		prediction = model.predict([[time, times, ta, rs, tin_windavg, tin_dooravg, setpoint]])

		label = str(np.squeeze(prediction))

		if label=='10': label='0'
		
		return render_template('index.html', label=label)


if __name__ == '__main__':

	model = joblib.load('model.pkl')
	app.run(host='0.0.0.0', port=8000, debug=True)