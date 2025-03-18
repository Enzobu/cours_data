import pandas as pd                                                     # type: ignore
from sklearn.model_selection import train_test_split                    # type: ignore
from sklearn.linear_model import Ridge                                  # type: ignore
from sklearn.metrics import mean_absolute_error, mean_squared_error     # type: ignore
import numpy as np                                                      # type: ignore

def predict(matrix):
    matrix = pd.DataFrame(matrix, columns=["country", "meal_inexpensive", "meal_for_two", "mcmeal", "domestic_beer", "imported_beer", "cappuccino", "coke_pepsi", "water_small", "milk", "bread", "rice", "eggs", "cheese", "chicken", "beef", "apples", "banana", "oranges", "tomato", "potato", "onion", "lettuce", "water_large", "non_alcoholic_wine", "cigarettes", "local_transport_ticket", "monthly_pass", "taxi_start", "taxi_per_km", "taxi_waiting", "gasoline", "volkswagen_golf", "toyota_corolla", "utilities", "mobile_plan", "internet", "fitness_club", "tennis_court", "cinema", "preschool", "primary_school", "jeans", "summer_dress", "nike_shoes", "leather_shoes", "apt_1bed_city", "apt_1bed_out", "apt_3bed_city", "apt_3bed_out", "price_sq_m_city", "price_sq_m_out", "net_salary", "crime_index"])

    if 'crime_index' not in matrix.columns:
        raise ValueError("La colonne 'crime_index' n'existe pas dans la matrice")

    X = matrix.drop(columns=['country', 'crime_index'])
    y = matrix['crime_index']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = Ridge(alpha=1.0)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print("Évaluation du modèle :")
    print(f"MAE (Mean Absolute Error): {mae}")
    print(f"MSE (Mean Squared Error): {mse}")
    print(f"RMSE (Root Mean Squared Error): {rmse}")

    countries = X_test.index
    country_predictions = pd.DataFrame({'country': matrix.iloc[countries]['country'], 'predicted_crime_index': y_pred})

    return model, country_predictions