import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.cluster import AffinityPropagation
from sklearn import metrics

from sklearn.datasets.samples_generator import make_blobs

from sklearn import preprocessing

from xlrd import open_workbook

filename = 'data.xls'
workbook = open_workbook(filename)
sheet = workbook.sheets()[0]

records = []
nrows = sheet.nrows
ncols = sheet.ncols
dimensions = [sheet.cell(0, col).value for col in range(1, ncols)]

print
data = {}

for row in range(1, sheet.nrows):
    series = []
    for col in range(sheet.ncols):
        cell_value = sheet.cell(row,col).value

        if col == 0:
            series_name = cell_value
        else:
            series.append(cell_value)

    data[series_name] = pd.Series(series, index=dimensions, dtype='int32')

dataframe = pd.DataFrame(data)
dataframe = dataframe.transpose()
X = dataframe.as_matrix()


# Compute Affinity Propagation
af = AffinityPropagation(preference=-50).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print('Estimated number of clusters: %d' % n_clusters_)
records = dataframe.to_records()

for i in range(len(labels)):
    print 'cluster' labels[i], records[i]