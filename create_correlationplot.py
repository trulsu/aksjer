import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import os
import pandas as pd
import numpy as np

# sentdex - Preprocessing data for Machine Learning
# Python Programming for Finance p. ?

style.use('ggplot')

# If a company is correlated to another and the first
# rises, the second will probably do so soon!
# This creates a heatmap that shows positive correlation
# as green, and negative correlation as red
def visualize_data():
	df = pd.read_csv('oslobors_joined_closed.csv')
	df_corr = df.corr() # Correlation table to the data
	data = df_corr.values
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn) #RedYellowGreen
	fig.colorbar(heatmap)
	ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
	ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
	ax.invert_yaxis()
	ax.xaxis.tick_top()
	
	column_labels = df_corr.columns
	row_labels = df_corr.index
	
	ax.set_xticklabels(column_labels)
	ax.set_yticklabels(row_labels)
	plt.xticks(rotation=90)
	heatmap.set_clim(-1,1)
	plt.tight_layout()
	plt.show()

visualize_data()
