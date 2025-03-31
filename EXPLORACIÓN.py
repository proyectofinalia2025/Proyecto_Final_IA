drive.mount('/content/drive')
file_path = "/content/drive/MyDrive/base proyecto final.xlsx"
df = pd.read_excel(file_path)
df
df.describe()
df.info()
df['ÁREA DE CONOCIMIENTO'].value_counts()
df['GRADUADOS'].value_counts()
