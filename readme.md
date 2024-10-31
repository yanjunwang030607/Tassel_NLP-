# DIN-SQL: Decomposed In-Context Learning of Text-to-SQL withSelf-Correction

#### 内容列表：
* [Introduction](#Introduction)
* [数据database](#数据database)
* [Setup](#Setup)

## Introduction：

DIN-SQL-main文件用于调用gpt4或智谱大模型，生成1034条sql预测结果并提取为txt文件，主代码文件为：DIN-DQL.py

test-suite-sql-eval-master用于根据不同模型生成的预测数据和真实数据做对比评估，计算具体全方面准确率，主代码文件为：evaluation.py

## 数据database：
(以下4条数据操作已全部完成，文件夹已全都包含，仅用于说明）

#### 1：需要到以下网址下载Sprider数据集：
```
Spider数据集="https://drive.google.com/uc?export=download&id=1TqleXec_OykOYFREKKtschzY29dUcVAQ"
```
#### 2：将其中dev.json和tables.json文件复制合并为一个文件夹并命名为[data]，置于DIN-SQL-main文件夹中。把tables.json文件再复制一份到test-suite-sql-eval-master文件夹中。
#### 3：将其中的database文件整个复制到test-suite-sql-eval-master文件夹中，不改变命名。
#### 4：将不同模型生成的预测数据txt文件和真实准确数据txt文件放到test-suite-sql-eval-master/evaluation_examples文件夹中。如：zhipuai_predict.txt；gold.txt。


## Setup：

### 1：配置环境
DIN-SQL-main所需包:
>pip install -r requirements.txt

智谱ai大模型智谱ai所需包
>pip install zhipuai

test-suite-sql-eval-master所需包：

sql执行器测试套件：
>pip install sqlparse

自然语言工具包：

>import nltk

编辑：nltk.download()

### 2：运行操作：
#### （1）：在DIN-SQL-main生成预测数据指令：(本文件已完成)
(data后为database文件，output后为生成预测数据的文件，以 predicted_sql.txt为例)
> python DIN-SQL.py --dataset ./data/ --output predicted_sql.txt 
#### （2）：将生成的预测txt文件提取为符合评估使用的txt文件。(本文件已完成)
(Withdraw.py中两个文件路径分别为生成的预测数据txt文件和符合评估使用的txt文件)
>python Withdraw.py


#### （3）：在test-suite-sql-eval-master文件夹中运行evaluation.py文件，计算准确率。
(文件说明：evaluation_examples文件夹中需有不同模型生成的预测数据zhipuai_predict.txt;GPT4_predict.txt;GPT4_few_shot.txt等文件和真实准确数据gold.txt文件)
##### 命令：



>python .\evaluation.py --gold .\evaluation_examples\gold.txt  --pred .\evaluation_examples\DIN_predict.txt --db .\database\ --table .\tables.json --etype all

以上四个参数分别为：
```
--gold .\evaluation_examples\gold.txt：真实准确数据gold.txt文件
--pred .\evaluation_examples\DIN_predict.txt模型生成的已符合格式要求的预测数据文件，以DIN_predict.txt为例。
--db .\database\ ：database文件
--table .\tables.json ：tables.json文件
--etype all：指标准确率类型，有exce，match和all三种。
```