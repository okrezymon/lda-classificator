import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt
# import pandas as pd
import globals
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle5 as pickle
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression


def classifier():

    X = globals.feature_arr
    Y= globals.labels

    # Spltting data into training and testing sets and shuffling them
    X_train,X_test,y_train,y_test = train_test_split(X, Y, test_size = 0.3)

    # lda = LDA()
    # X_lda = lda.fit_transform(X_train, y_train)
    #
    # plt.xlabel('LDA1')
    # plt.ylabel('LDA2')
    # plt.scatter(
    #     X_lda[:, 0],
    #     X_lda[:, 1],
    #     c=y_train,
    #     cmap='rainbow',
    #     alpha=0.7,
    #     edgecolors='b'
    # )

    # fit a LinearDiscriminantAnalysis() model to the data
    # model = LDA()
    # model.fit(X_train, y_train)
    # print();
    # print(model)
    #
    # # make predictions
    # expected_y = y_test
    # predicted_y = model.predict(X_test)
    #
    # # summarize the fit of the model
    # print();
    # print('LinearDiscriminantAnalysis(): ')
    # print();
    # print(metrics.classification_report(expected_y, predicted_y))
    # print();
    # print(metrics.confusion_matrix(expected_y, predicted_y))
    # print(model.predict([X_test[5]]))
    # print(y_test[5])
    #
    # # save model to a file
    # filename = 'lda_model.sav'
    # pickle.dump(model, open(filename, 'wb'))
    #
    # load model from a file
    loaded_model = pickle.load(open('lda_model.sav', 'rb'))
    result = loaded_model.score(X_test, y_test)
    print(result)
    print(loaded_model.predict([X_test[5]]))
    print(y_test[5])


    # Visualising the Regression Result on Training Set

    # X_set, y_set = X_train, y_train
    # X1,X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),np.arange(start=X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
    # plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    #              alpha=0.75, cmap=ListedColormap(('red', 'green', 'blue')))
    # plt.xlim(X1.min(), X1.max())
    # plt.ylim(X2.min(), X2.max())
    # for i, j in enumerate(np.unique(y_set)):
    #     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
    #                 c=ListedColormap(('red', 'green', 'blue'))(i), label=j)
    # plt.title('Logistic Regression(Training set)')
    # plt.xlabel('LD1')
    # plt.ylabel('LD2')
    # plt.legend()
    # plt.show()







    # # Implementation of LDA
    # lda = LDA(n_components=11)
    # lda.fit(X_train, y_train)
    #
    # # Predicting results of regression with LDA
    # y_prob_lda = lda.predict_proba(X_test)[:,1]
    # y_pred_lda = np.where(y_prob_lda>0.5,1,0)
    #
    # # Printing confusion matrix
    # confusion_matrix = metrics.confusion_matrix(y_test, y_pred_lda)
    # print(confusion_matrix)
    #
    # # Plotting the ROC curve nd get the area under the curve
    # false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test,y_prob_lda)
    # roc_auc_lda = auc(false_positive_rate, true_positive_rate)
    # print(roc_auc_lda)
    #
    # auc_roc = metrics.roc_auc_score(y_test,y_pred_lda)
    # print(auc_roc)






