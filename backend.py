import pandas
import numpy as np
import requests
from bokeh.plotting import figure
from bokeh.io import output_file
from bokeh.embed import components
from bokeh.resources import CDN

def datetime(x):
    return np.array(x, dtype=np.datetime64)


def get_data(ticker):
	ticker = ticker.upper()
	url = "https://www.quandl.com/api/v3/datasets/WIKI/{ticker}/data.json".format(ticker=ticker)
	r = requests.get(url)
	return pandas.DataFrame(data=r.json()['dataset_data']['data'], columns=r.json()['dataset_data']['column_names'])
	
def get_graph(df, checkboxes, ticker):
	output_file('boken_file.html')
	x = df.Date

	p = figure(x_axis_type="datetime")
	p.xaxis.axis_label = 'Date'

	if checkboxes.op:
		p.line(datetime(x), df.Open, color='#A6CEFF', legend='Open Price ')
	if checkboxes.aop:
		p.line(datetime(x), df['Adj. Open'], color='#CB112A', legend='Adj. Open Price')
	if checkboxes.cp:
		p.line(datetime(x), df.Close, color='#FF9A99', legend='Close Price')
	if checkboxes.acp:
		p.line(datetime(x), df['Adj. Close'], color='#33A02C', legend='Adj. Close Price')
	
	script, div = components(p, CDN)
	return script, div