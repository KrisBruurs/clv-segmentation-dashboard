import pandas as pd
import requests
import zipfile
import io
from pathlib import Path

Path("data").mkdir(exist_ok=True)

url = "https://absentdata.com/wp-content/uploads/2024/08/customer_zip_data.zip"

req = requests.get(url)
zip = zipfile.ZipFile(io.BytesIO(req.content))
zip.extractall("data")