import seaborn as sns
import pandas as pd
import numpy as np
dataset=sns.load_dataset("iris")
print(sns.pairplot(dataset,hue="species"))