from django.shortcuts import render
from django.http import HttpResponse
import worker
from pickleTest import regressor
import numpy as np

# Create your views here.


def index(request):
    return render(request, 'input.html', {'teams': worker.teams, 'venues': worker.venues})


def result(request):

    temp_array = list()

    temp_array = temp_array + worker.hotTeam(request.POST['bat_team'])
    temp_array = temp_array + worker.hotTeam(request.POST['bowl_team'])
    venue = worker.hotVenue(request.POST['venue'])
    temp_array.append(venue)
    runs = int(request.POST['runs'])
    temp_array.append(runs)
    wickets = int(request.POST['wickets'])
    temp_array.append(wickets)
    overs = float(request.POST['overs'])
    temp_array.append(overs)
    runs_in_prev_5 = int(request.POST['runs_in_prev_5'])
    temp_array.append(runs_in_prev_5)
    wickets_in_prev_5 = int(request.POST['wickets_in_prev_5'])
    temp_array.append(wickets_in_prev_5)
    data = np.array([temp_array])
    my_prediction = int(regressor.predict(data)[0])
    low = my_prediction - 10
    high = my_prediction + 4

    return render(request, 'result.html', {'low': low, 'high': high})
