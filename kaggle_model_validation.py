from kaggle_model_building import model_builder
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

def mae():

    '''This function calculates the mean absolute error'''

    # Get the model, X, and y from the first file
    melbourne_model, X, y = model_builder()

    #Calculating mean absolute error
    predicted_home_prices = melbourne_model.predict(X)
    mae = mean_absolute_error(y, predicted_home_prices)
    print(mae)

mae() # Output: 1125.18; has to be: 434.72


def model_splitter():

    ''' this function splits data into training and validation data,
    for both features and target
    The split is based on a random number generator. Supplying a numeric value to
    the random_state argument guarantees we get the same split every time we
    run this script '''

    melbourne_model, X, y = model_builder()
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
    # Define model
    melbourne_model = DecisionTreeRegressor()
    # Fit model
    melbourne_model.fit(train_X, train_y)

    # get predicted prices on validation data
    val_predictions = melbourne_model.predict(val_X)
    print(mean_absolute_error(val_y, val_predictions))

model_splitter()
