import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
from scipy.stats import ttest_ind

data = pd.read_csv('data.csv')

mean_b = np.mean(data["Conversion_B"]) #mean for conversion B

mean_a = np.mean(data["Conversion_A"]) #mean for conversion A

t_stat, p_stat = ss.ttest_ind(data.Conversion_B, data.Conversion_A)

print( mean_a, mean_b, t_stat, p_stat)#   A - B - t e s t i n g - T t e s t - w i t h - p y t h o n -  
 