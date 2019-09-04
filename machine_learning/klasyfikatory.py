# -*- coding: utf-8 -*-

from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import accuracy_score

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],[166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], 
     [181, 85, 43], [168, 75, 41], [168, 77, 41]]
Y = ['x', 'x', 'y', 'y', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'y', 'y']

test_data = [[190, 70, 43],[154, 75, 38],[181,65,40]]
test_labels = ['x','y','x']

dtc_tree_acc = 0
rfc_acc = 0
l_acc = 0
s_acc = 0
kNB_acc = 0

for i in range(100):
    
    # Drzewa decyzyjne

    dtc_clf = tree.DecisionTreeClassifier()
    dtc_clf = dtc_clf.fit(X,Y)
    dtc_prediction = dtc_clf.predict(test_data)
    #print(dtc_prediction)

    # Decyzyjny las losowy

    rfc_clf = RandomForestClassifier(n_estimators = 100)
    rfc_clf.fit(X,Y)
    rfc_prediction = rfc_clf.predict(test_data)
    #print(rfc_prediction)
    
    # Regresja logistyczna

    l_clf = LogisticRegression(solver = 'lbfgs')
    l_clf.fit(X,Y)
    l_prediction = l_clf.predict(test_data)
    #print(l_prediction)

    # SVC

    s_clf = SVC(gamma = 'scale')
    s_clf.fit(X,Y)
    s_prediction = s_clf.predict(test_data)
    #print(s_prediction)

    # k- najblizszych sasiadow

    kNB_clf = KNeighborsClassifier()
    kNB_clf.fit(X,Y)
    kNB_prediction = kNB_clf.predict(test_data)
    #print(kNB_prediction)

    # Dokładnosc

    dtc_tree_acc += accuracy_score(dtc_prediction,test_labels)
    rfc_acc += accuracy_score(rfc_prediction,test_labels)
    l_acc += accuracy_score(l_prediction,test_labels)
    s_acc += accuracy_score(s_prediction,test_labels)
    kNB_acc += accuracy_score(kNB_prediction,test_labels)

print('Drzewo decyzyjne', dtc_tree_acc, 'Decyzyjny las losowy', rfc_acc, 'Regresja logistyczna', l_acc, 'SVC', s_acc,'Najbliżsi sąsiedzi', kNB_acc)

klasyfikatory = ['Drzewo decyzyjne', 'Decyzyjny las losowy', 'Regresja logistyczna' , 'SVC','Najbliżsi sąsiedzi']
dokładnosc = np.array([dtc_tree_acc, rfc_acc, l_acc, s_acc, kNB_acc])
max_acc = np.argmax(dokładnosc)
print('\n' + klasyfikatory[max_acc] + ' jest najlepszym klasyfikatorem problemu.\n')

