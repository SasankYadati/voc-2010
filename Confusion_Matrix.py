from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
actual = [1, 2, 3, 1, 4, 0, 1, 0, 6, 5]
predicted = [1, 3, 2, 1, 0, 5, 1, 4, 1, 6]
results = confusion_matrix(actual, predicted)
print('Confusion Matrix :')
print(results)
print('Accuracy Score :',accuracy_score(actual, predicted))
print('Report : ')
print(classification_report(actual, predicted))
print('Class pairs with high confusion:')
high=1
for i in range(len(results)):
    for j in range(len(results)):
        if(results[i][j]>high):
            print(i,j)
