from kedro.pipeline import Pipeline
from kedro.nodes import Node

# Definir el nodo que carga el dataset de Excel
def load_excel_dataset():
    return pd.read_excel('Monopoly.xlsx')
# Definir el nodo que procesa el dataset
def process_dataset(dataset):
    # Procesar el dataset aquí
    return dataset

# Crear el pipeline
pipeline = Pipeline([
    Node(load_excel_dataset, inputs=None, outputs='dataset'),
    Node(process_dataset, inputs='dataset', outputs='processed_dataset')
])