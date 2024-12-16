import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file_path = '/home/mari/Documents/scripts/ML/melb_data.csv'

def model_builder():

    melbourne_data = pd.read_csv(melbourne_file_path)

    print("Describe: \n",melbourne_data.describe)
    print("Columns: \n",melbourne_data.columns)

    # Data subset selection (pulling out a variable)
    y = melbourne_data.Price #dot notation for prediction target (conventionally y)

    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'] #column list for features
    X = melbourne_data[melbourne_features] #features

    print("Describe features: \n",X.describe())
    print("Head of the features: \n", X.head())

    # Define model. Specify a number for random_state to ensure same results each run
    melbourne_model = DecisionTreeRegressor(random_state=1)

    # Fit model
    melbourne_model.fit(X, y)

    # Making predictions (training data as an exampe, usually new data)
    print("Making predictions for the following 5 houses: " )
    print(X.head())
    print("the predictions are: ")
    print(melbourne_model.predict(X.head()))

    return melbourne_model, X, y
