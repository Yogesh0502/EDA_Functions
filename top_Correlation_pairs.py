#!/usr/bin/env python
# coding: utf-8

# In[2]:

'''
get_redundant_pairs(df): This function is used to get the Diagonal and Triangular paris of correclation Matrix in a dataframe
get_top_abs_correlations(df, n=5) : This is used to get the top n Correlation paiirs.
'''

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop



def get_top_abs_correlations(df, n=5):
    '''Get the top correlation pairs. '''
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]


# In[ ]:




