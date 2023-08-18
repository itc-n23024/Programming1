import pickle

with open("test1.pkl", "rb") as f:
    awa = pickle.load(f)
    print(awa)
