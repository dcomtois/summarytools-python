# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 21:11:27 2018

@author: Dominic
"""
import re
import pandas as pd
import numpy as np
from numpy import nan
from tabulate import tabulate

class freq:
  """
  Frequency tables for categorical data.

  Keyword arguments:
  
  data    -- an iterable object containing numerical or character data
  digits  -- number of digits to show (default: 2)
  order   -- either 'names' (default) or 'value' - not implemented yet
  format  -- argument passed to tabulate. Common are: 'markdown' (default),
             'fancy_grid', 'html' and 'latex'. See tabulate documentation
             for more.
  totals  -- boolean; show totals row (default: True)
  nans    -- boolean; include missing data for reporting (default: True)
  weights -- not implemented yet
  
  """
  def __init__(self, data, # any iterable object with character or numeric data,
               digits = 2, # Number of rounding digits (defaults to 2)
               order = "names", # One of 'names' or 'values' 
               format = "markdown", # Format for tabulate display (defaults to 'markdown'). Common values
                                   # are 'pipe', 'grid', and 'fancy_grid'
               totals = True, # Display last line of table containing totals (defaults to True)
               nans = True, # Report missing data (NaN/None). Defaults to True.
               weights = nan # Not implemented yet
               ):
                 
    self.digits  = digits
    self.order   = order
    self.format  = format
    self.totals  = totals
    self.nans    = nans
    self.weights = weights
    
    
    # If numeric, replace all non-finite with np.nan
    if re.search('float', type(data[0]).__name__) != None:
      data = np.array(data)
      data[pd.isnull(data)] = nan
    elif re.search('int', type(data[0]).__name__) != None:
      data = np.array(data) # no need to replace here, NaN can't be in an integer array
    elif re.search('str', type(data[0]).__name__) != None:
      data = pd.Categorical(data)
      data[pd.isnull(data)] = nan
    else:
      print("Data type not recognized")
      return None
    
    counts = pd.value_counts(pd.Categorical(data), dropna=False, sort=False)
    rownames = list(counts.index)
    has_nans = any(pd.isna(rownames))
    if has_nans:
      rownames.pop(-1)

    rownames.extend(('NaN','Total'))

    # Calculate frequencies when weights are not used
    if not all(np.isnan(weights)):
      for i in range(0, len(rownames) - 2):
        counts[i] = sum(counts[0] * weights[data == rownames[0]])
      counts[-1] = sum(counts[-1] * weights[np.isnan(data)])
    
    # Calculate proportions
    prop_total = counts/np.asscalar(counts.sum())
    prop_total_cum = prop_total.cumsum()
    prop_total_cum[-1] = 1 # in case of rounding causing .999    

    if has_nans:
      prop_valid = pd.value_counts(data, dropna=True, sort=False) / \
                     np.asscalar(counts[0:len(counts)-1].sum())
      prop_valid_cum = prop_valid.cumsum()
      prop_valid_cum[-1] = 1 # in case of rounding causing .999
    else:
      prop_valid = prop_total
      prop_valid_cum = prop_total_cum


    # Convert elements to regular lists and add pertinent values
    counts = counts.tolist()
    counts.append(sum(counts))
  
    prop_total = (prop_total * 100).tolist()
    prop_total.append(100)
  
    prop_total_cum = (prop_total_cum * 100).tolist()
    prop_total_cum.append(100)
  
    prop_valid = (prop_valid * 100).tolist()
    prop_valid.extend((None, 100))
    
    prop_valid_cum = (prop_valid_cum * 100).tolist()
    prop_valid_cum.extend((None,100))

    if not has_nans:
      counts.insert(-1, 0)
      prop_total.insert(-1, 0)
      prop_total_cum.append(100)


    # Prepare output Dataframe
    output = np.full((len(counts), 5), None)  
    output[:,0] = counts
    output[:,1] = prop_valid
    output[:,2] = prop_valid_cum
    output[:,3] = prop_total
    output[:,4] = prop_total_cum

    output = pd.DataFrame(output)
    output.index = rownames
    output.columns = ["Freq", "% Valid", "% Valid Cum.", "% Total", "% Total Cum."]

    self.output = output
  
  def __repr__(self):    
    if not self.nans:
      self.output.Freq[-1] -= self.output.Freq[-2]
      self.output = self.output.drop('NaN')
      self.output = self.output.drop("% Total", axis = 1)
      self.output = self.output.drop("% Total Cum.", axis = 1)
      #self.output.columns = ["Freq", "%", "% Cum."]
    
    if not self.totals:
      self.output = self.output.drop('Total')
      
    return tabulate(self.output, tablefmt = self.format, headers = 'keys',
                      floatfmt = '.' + str(self.digits) + 'f')
  
  def print(self, digits = None, order = None, format = None, totals = None, nans = None):
    """
    Print frequency table, optionnaly using temporary settings for format etc.
    """
    digits = next(i for i in [digits, self.digits] if i is not None)
    order  = next(i for i in [order,  self.order]  if i is not None)
    format = next(i for i in [format, self.format] if i is not None)
    totals = next(i for i in [totals, self.totals] if i is not None)
    nans   = next(i for i in [nans,   self.nans]   if i is not None)

    output = self.output
    
    if not nans:
      output.Freq[-1] -= output.Freq[-2]
      output = output.drop('NaN')
      output = output.drop("% Total", axis = 1)
      output = output.drop("% Total Cum.", axis = 1)
    
    if not totals:
      output = output.drop('Total')
      
    print(tabulate(output, tablefmt = format, headers = 'keys',
                   floatfmt = '.' + str(digits) + 'f'))
    
    return None
