#Making predictions

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred=np.rint(y_pred)       


#Evaluating the model
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



