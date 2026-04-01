import kagglehub
import os

path = kagglehub.dataset_download("jayavarman/synthetic-car-sales-dataset-over-million-records")

csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
dataset_file = os.path.join(path, csv_files[0])
print("Dataset downloaded to:", dataset_file)
