from django.apps import AppConfig
import pandas as pd
import os

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    data_path = os.path.join(os.path.dirname(__file__),"brand_data.csv")
    data = None
    
    def ready(self):
        self.data = pd.read_csv(self.data_path)