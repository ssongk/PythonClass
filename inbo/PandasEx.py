import pandas as pd
import numpy as np
from pyparsing import col
dfA=pd.DataFrame(np.arange(16).reshape(4,4))
dfB=pd.DataFrame([[1,0,0,0],
                  [0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,1]])
print(dfA.dot(dfB))
