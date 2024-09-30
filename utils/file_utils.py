import pandas as pd

def read_names_from_csv(filepath):
    df = pd.read_csv(filepath, header = None)
    names_list = [j[0] for i, j in df.iterrows()]
    return names_list

['Adheeba', 'Anastasiia', 'Basma', 'Dhrisya', 'Ihor', 'Izabela', 'Kelli', 'Kevin', 'Levin', 'Maarten',
  'Majid', 'Minh Duc', 'Moustafa', 'Muntadher', 'Nicolaas', 'Petra', 
  'Rasmita', 'Rik', 'Soha', 'Tom', 'Urson', 'Veena', 'Wouter', 'Yeliz', 'Yusra', 'Zelimkhan']