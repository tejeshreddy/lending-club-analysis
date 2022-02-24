# Core Dependencies
import re
import os


# Start Python Imports
import math, time, random, datetime

# Data Manipulation
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.display.min_rows = 200

# Visualization 
import matplotlib.pyplot as plt
import missingno
import seaborn as sns
plt.style.use('seaborn-whitegrid')

import warnings
warnings.filterwarnings("ignore")


class EDA:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def plot1(data):
        fig = missingno.matrix(data)
        return fig
    
    @staticmethod
    def plot2(data):
        fig = plt.figure(figsize=(20,5))
        sns.countplot(y='loan_status', data=data);

    
    @staticmethod
    def plot3(data):
        fig = plt.figure(figsize=(20,5))
        sns.heatmap(acc_df.corr(), annot=True, cmap='viridis');
    
    @staticmethod
    def plot4(data):
        fig = plt.figure(figsize=(20, 4))
        sns.countplot(y="grade", data=data)
    
    @staticmethod
    def plot5(data):
        fig = plt.figure(figsize=(10, 10))
        sns.histplot(data=data, x="installment", bins=30, kde=True, hue="loan_status")
    
    
    @staticmethod
    def plot6(paid_charged):
        plt.figure(figsize=(15, 20))

        plt.subplot(4, 2, 1)
        sns.countplot(x='term', data=paid_charged, hue='loan_status')

        plt.subplot(4, 2, 2)
        sns.countplot(x='home_ownership', data=paid_charged, hue='loan_status')

        plt.subplot(4, 2, 3)
        sns.countplot(x='verification_status', data=paid_charged, hue='loan_status')

        plt.subplot(4, 2, 4)
        g = sns.countplot(x='purpose', data=paid_charged, hue='loan_status')
        g.set_xticklabels(g.get_xticklabels(), rotation=90);
    
    @staticmethod
    def plot7(paid_charged):
        plt.figure(figsize=(15, 10))

        plt.subplot(2, 2, 1)
        grade = sorted(paid_charged.grade.unique().tolist())
        sns.countplot(x='grade', data=paid_charged, hue='loan_status', order=grade)

        plt.subplot(2, 2, 2)
        sub_grade = sorted(paid_charged.sub_grade.unique().tolist())
        g = sns.countplot(x='sub_grade', data=paid_charged, hue='loan_status', order=sub_grade)
        g.set_xticklabels(g.get_xticklabels(), rotation=90);
    
    @staticmethod
    def plot8(paid_charged):
        plt.figure(figsize=(8, 6))
        order = ['< 1 year', '1 year', '2 years', '3 years', '4 years', '5 years', 
                  '6 years', '7 years', '8 years', '9 years', '10+ years',]
        g = sns.countplot(x='emp_length', data=paid_charged, hue='loan_status', order=order)
        g.set_xticklabels(g.get_xticklabels(), rotation=90);
    
    @staticmethod
    def plot9(paid_charged):
        plt.figure(figsize=(8, 6))
        plt.barh(paid_charged.emp_title.value_counts()[:40].index, paid_charged.emp_title.value_counts()[:40])
        plt.title("The most 30 jobs title afforded a loan")
        plt.tight_layout()
    
    @staticmethod
    def plot10(paid_charged):
        plt.figure(figsize=(8, 6))
        sns.countplot(x="application_type", data=paid_charged, hue="loan_status")


        

    
