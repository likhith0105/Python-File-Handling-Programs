import pickle

data = [
    {'name': 'geek', 'score': 10},
    {'platform': 'GeeksforGeeks', 'rating': 4.8},
    {'username': 'supergeek', 'active': False}
]

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)