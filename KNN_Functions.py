# Pandas adn Numpy imports
import pandas as pd
import numpy as np

# scikit learn scalers, train_test_split, K Nearest Neighbors Classifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Function to separate the Pandas Dataframe into X and y variables
def DataFrame_to_X_and_y(DataFrame):
    """
    Take a DataFrame and split it by [:1] and [1:] for y and X variables.
    A key assumption is that the First Column are the labels and the rest are the feature variables.
    """
    X = DataFrame.iloc[:, 1:]
    y = DataFrame.iloc[:, :1]
    return X, y

# Function to Train Test Split the Data and apply a scaler if needed
# returns all train, test features and targets including the scaler if needed
def Train_Test_Split_and_Scale(features, labels, scaler=None, random_state=42, test_size=0.25):
    """
    Pass in features (X) and labels (y) as appropriately shaped DataFrames or Numpy Arrays.
    Obtain X_train, y_train, X_test and y_test.
    Options are having them scaled if passing a scaler, setting the random_state and setting the test_size.
    """
    # train_test_split from SciKit learn is applied on the feature and labels
    (X_train, X_test,
     y_train, y_test) = train_test_split(features, labels,
                                         random_state=random_state,
                                         test_size=test_size)
    # if a scaler from SciKit learn is passed then apply it to X_train
    if scaler:
        # try to scale X_train and transform X_train and X_test with passed in scaler
        try:
            scaler.fit(X_train)
            # supress warnings for SettingCopywithWarning
            with pd.option_context("mode.chained_assignment", None):
                # maintain dataframe structure
                X_train.loc[:,:] = scaler.transform(X_train.values)
                X_test.loc[:,:] = scaler.transform(X_test.values)
                # return the following values
                return (X_train, X_test, y_train, y_test, scaler)
        except:
            print("Passed in scaler does not have .fit() and .transform() methods.\nReturn values from train_test_split() method.")
            return (X_train, X_test, y_train, y_test, scaler)
    else:
        # return values from train_test_split() method
        return (X_train, X_test, y_train, y_test, scaler)
    
# create Function that will create an instance of the KNN model, have it fitted to training data
# and return the fitted model
def K_Nearest_Neighbours_Model(train_features, train_labels, k_value=5, algorithm_auto="auto"):
    """
    Instantiate the K Nearest Neighbors (KNN) Classifier Model with a k_value and provided X_train and y_train (Pandas DataFrames).
    Return KNN model that has been .fit() with training data.
    """
    # create an instance of the KNN SciKit learn class
    model = KNeighborsClassifier(n_neighbors=k_value, algorithm=algorithm_auto)
    # fit the model to the training data and labels
    model.fit(train_features, train_labels.values.ravel())
    # return the .fit() model
    return model

# take the fitted model and return its score for Training Data and Testing Data
# and Training data predictions and Testing data predictions
def Scores_And_Predictions(train_features, train_labels, test_features, test_labels, model, prediction_flag=False):
    """
    Take the Fitted KKN Classifier Model and provide training and testing data scores.
    Also return training and testing label predictions.
    """
    # get the training and testing data scores
    train_score = model.score(train_features, train_labels.values.ravel())
    test_score = model.score(test_features, test_labels.values.ravel())
    # get the training and testing predictions
    train_predict = model.predict(train_features)
    test_predict = model.predict(test_features)
    # if True then output the predictions
    if prediction_flag:
        # return the 4 values
        return (train_score, test_score, train_predict, test_predict)
    else:
        return (train_score, test_score, None, None)