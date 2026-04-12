import requests
import zipfile
import io
import pandas as pd



url = 'https://survey.stackoverflow.co/datasets/stack-overflow-developer-survey-2025.zip'
survey =  requests.get(url)


with zipfile.ZipFile(io.BytesIO(survey.content)) as f:
    print(f.namelist())
    with f.open('survey_results_public.csv') as f:
        df = pd.read_csv(f)
        print(df.head())


