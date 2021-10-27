import pandas as pd

# create dataframe
df = pd.read_csv("C:\Users\Nick\Documents\School\Homework\Web-Design-Challenge\WebVisualisation\Resources\cities.csv")
df.to_html('Cities.html')

# render dataframe as html
html = df.to_html()
print(html)