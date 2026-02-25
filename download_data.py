import kagglehub
import shutil
import os
from pathlib import Path
import glob

Path("data").mkdir(exist_ok=True)

path = kagglehub.dataset_download("mashlyn/online-retail-ii-uci")

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")
dest_path = os.path.join(data_dir, "customer_data.csv")

csv_files = glob.glob(os.path.join(path, "*.csv"))
shutil.copy(csv_files[0], dest_path)
print(f"Saved to {dest_path}")