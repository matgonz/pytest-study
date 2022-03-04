from sklearn.linear_model import LinearRegression
from joblib import dump, load

import numpy as np

def train_dummy_model():
    print("Training Linear Regression model")

    X_train = np.array([1, 3, 5, 7, 9]).reshape(-1,1)
    y_train = np.array([10, 30, 50, 70, 90]).reshape(-1,1)

    # train our model
    model = LinearRegression()
    model.fit(X_train, y_train)

    dump(model, 'trained_linear_regression_model.sav')

if __name__ == "__main__":
    train_dummy_model()