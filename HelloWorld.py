# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:40:58 2021

@author: AK
"""

from sklearn import tree


def predictFruit():
    """ first step is to create the training data for example features and labels , 
        second step to train the classifier with the training data 
        third step to predict by givin input """
    features=[[140,1],[130,1],[345,0],[560,0]]
    lables = [1,1,0,0]
    
    # this is just a classifier till now and dont know anything about the input for eg apple or oranges till now
    # so we need a machine learing algorthim now to train this callsifier with training data
    # if you think classifier as a set of rules then think machine learning is a procedure that create 
    # them and it does by finding pattern in the traing data
    
    clf=tree.DecisionTreeClassifier()
    
    # in skleran this classifier comes up with training algorthim like below
    clf.fit(features, lables)

    # finally predict the result by providing input data 0 for orange and 1 for applie, try diffrent combinations
    print (clf.predict([[50,0]]))


predictFruit()