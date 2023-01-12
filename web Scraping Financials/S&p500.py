import pickle as pkl

data = []
with open("s&p500_companies_data.pickle","rb") as f:
    data = pkl.load(f)
print(data[1])