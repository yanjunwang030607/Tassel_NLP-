import pandas as pd
import numpy as np
file1=pd.read_csv(r'D:\Desktop\DIN-SQL-main\\GPT4_results\GPT4_zero_shot.csv')
file1=np.array(file1)
with open(r'D:\Desktop\DIN-SQL-main\\predict_gpt4.txt','w') as f:
    for i in range(0,1034):
        f.write(file1[i][1]+'\n')
