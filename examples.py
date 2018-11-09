# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 23:08:32 2018

@author: Dominic
"""
import pandas as pd
import numpy as np
tobacco = pd.read_csv("data/tobacco.csv", encoding='ansi')

freq(tobacco.age_gr)
freq(tobacco.age_gr, nans = False)
freq(tobacco.age_gr, totals = False)

ft = freq(tobacco.gender, format = 'fancy_grid')
ft.print(digits=1)
ft.print(nans=False)
ft.print(totals=False)

color_list = np.array(('White', 'Black', 'Blue', 'Red', 'Yellow'))
colors = color_list[np.random.randint(low = 0, high = 4, size = 500)]
freq(colors)

d = [i for i in range(0,10)]
freq(d)
