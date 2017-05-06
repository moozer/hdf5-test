import pandas as pd

dataset='SmaData_20160907'

df = pd.read_csv(dataset+'.csv', delimiter='\t')
df.to_hdf(dataset+'.hdf', dataset, mode="w")
df.to_hdf(dataset+'_comp.hdf', dataset, mode="w", complevel=9, complib='zlib')
