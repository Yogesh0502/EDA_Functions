{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "List highest correlation pairs for large Correlation Matrix\n",
    "'''\n",
    "\n",
    "import pandas as pd\n",
    "d = {'x1': [1, 4, 4, 5, 6], \n",
    "     'x2': [0, 0, 8, 2, 4], \n",
    "     'x3': [2, 8, 8, 10, 12], \n",
    "     'x4': [-1, -4, -4, -4, -5]}\n",
    "df = pd.DataFrame(data = d)\n",
    "print(\"Data Frame\")\n",
    "print(df)\n",
    "print()\n",
    "\n",
    "print(\"Correlation Matrix\")\n",
    "print(df.corr())\n",
    "print()\n",
    "\n",
    "def get_redundant_pairs(df):\n",
    "    '''Get diagonal and lower triangular pairs of correlation matrix'''\n",
    "    pairs_to_drop = set()\n",
    "    cols = df.columns\n",
    "    for i in range(0, df.shape[1]):\n",
    "        for j in range(0, i+1):\n",
    "            pairs_to_drop.add((cols[i], cols[j]))\n",
    "    return pairs_to_drop\n",
    "\n",
    "\n",
    "\n",
    "def get_top_abs_correlations(df, n=5):\n",
    "    '''Get the top correlation pairs. '''\n",
    "    au_corr = df.corr().abs().unstack()\n",
    "    labels_to_drop = get_redundant_pairs(df)\n",
    "    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)\n",
    "    return au_corr[0:n]\n",
    "\n",
    "print(\"Top Absolute Correlations\")\n",
    "print(get_top_abs_correlations(df, 3))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
