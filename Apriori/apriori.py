'''Apriori is all about the person who bought also bought... .This is just like recommendations.some of the practical examples 
are netflix,flikart.In this programme i am going to frame a set of logics or recommendations based on our customer datasets of 
the unknown super market.In apriori there are three important parameters to look for and they are ariori support,confidence and 
lift.In short  apriori support means that how many times the particular combination of the products are bought in a day.For ex 
in our problem we set the minimum support as 0.003(3*7/7500).Then confidence gives the info about how much percent the particular 
products are bought.Then lift shows the relavance percentage of the products.Min_lengh is set as 2 for our problem bcz we need to 
take atleast two products otherwise it doesn't make any sense.  
'''
# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)#header is none because in our dataset no title is present
transactions = []#creating list to put our transactions into it
for i in range(0, 7501):#to deal with all the transactions(rows)
        transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
        
#training the apriori
from apyori import apriori#library for the apriori model
logics = apriori(transactions,min_support = 0.003,min_confidence = 0.2,min_lift = 3,min_length = 2 )#conditions for our problem

#visualizing our results
results = list(logics)#recommendations from our apriori is created as a list
rules_list = []#empty list to visualize our recommended products and the apriori parameters 

for i in range(len(results)):

    rules_list.append('RULE:\t' + str(results[i][0]) +

                        '\nSUPPORT:\t' + str(results[i][1]) +

                        '\nCONFIDENCE:\t' + str(results[i][2][0][2]) +

                        '\nLIFT:\t' + str(results[i][2][0][3]))


  