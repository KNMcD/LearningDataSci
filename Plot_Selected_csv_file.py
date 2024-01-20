import pandas as pd
import plotly.express as px
Symbol = input('Enter ETF Symbol:')
Folder = 'C:\\Users\\Keith\\Desktop\\Files\\Patternz712\\ETFs\\'
File = Folder + Symbol + '.csv'
#print(File)
Header = Symbol + ' Closing Price'
df = pd.read_csv(File)
fig = px.line(df, x = 'Date', y = 'Close', title = Header)
fig.show()