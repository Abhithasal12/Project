# Importing the dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic_data = pd.read_csv('D:\Abhishek\Abhi_Code\FSDI_GEN-AI\Py_test\Python Project\Project\ML project\Titanic-Dataset.csv')
titanic_data.head()