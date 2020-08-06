import pickle
import numpy as np
from worker import hotVenue, hotTeam

# Load  model
filename = 'models/ridgeRegModel.pkl'
with open(filename, 'rb') as f:
    regressor = pickle.load(f)


if __name__ == "__main__":
    temp_array = list()
    temp_array = temp_array + hotTeam('Kolkata Knight Riders')
    temp_array = temp_array + hotTeam('Royal Challengers Bangalore')
    venue = hotVenue('M Chinnaswamy Stadium')
    temp_array.append(venue)
    runs = 70
    temp_array.append(runs)
    wickets = 1
    temp_array.append(wickets)
    overs = 6.1
    temp_array.append(overs)
    runs_in_prev_5 = 60
    temp_array.append(runs_in_prev_5)
    wickets_in_prev_5 = 1
    temp_array.append(wickets_in_prev_5)

    data = np.array([temp_array])
    print(data)
    my_prediction = int(regressor.predict(data)[0])
    print(my_prediction)
