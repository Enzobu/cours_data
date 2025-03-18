from matrix.getMatrix import getMatrix
from predict.predict import predict
from db.getDataFromDb import getDataFromDb


matrix = getDataFromDb('matrix_cost_of_life')
model, predictions = predict(matrix)

print("Premières prédictions du modèle :")
print(predictions[:10])

# getMatrix()
