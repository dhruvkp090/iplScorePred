teams = ['Chennai Super Kings', 'Delhi Capitals',
         'Kings XI Punjab', 'Kolkata Knight Riders',
         'Mumbai Indians', 'Rajasthan Royals',
         'Royal Challengers Bangalore',
         'Sunrisers Hyderabad']

venues = ['M Chinnaswamy Stadium',
          'Punjab Cricket Association Stadium, Mohali', 'Feroz Shah Kotla',
          'Wankhede Stadium', 'Eden Gardens', 'Sawai Mansingh Stadium',
          'Rajiv Gandhi International Stadium, Uppal',
          'MA Chidambaram Stadium, Chepauk', 'Dr DY Patil Sports Academy',
          'Newlands', "St George's Park", 'Kingsmead', 'SuperSport Park',
          'Buffalo Park', 'New Wanderers Stadium', 'De Beers Diamond Oval',
          'OUTsurance Oval', 'Brabourne Stadium',
          'Sardar Patel Stadium, Motera', 'Barabati Stadium',
          'Vidarbha Cricket Association Stadium, Jamtha',
          'Himachal Pradesh Cricket Association Stadium', 'Nehru Stadium',
          'Holkar Cricket Stadium',
          'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
          'Subrata Roy Sahara Stadium',
          'Shaheed Veer Narayan Singh International Stadium',
          'JSCA International Stadium Complex', 'Sheikh Zayed Stadium',
          'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
          'Maharashtra Cricket Association Stadium',
          'Punjab Cricket Association IS Bindra Stadium, Mohali',
          'Saurashtra Cricket Association Stadium', 'Green Park']
teamsHot = {}
venuesHot = {
    'Eden Gardens': 4770,
    'M Chinnaswamy Stadium': 4681,
    'Feroz Shah Kotla': 4636,
    'Wankhede Stadium': 4435,
    'MA Chidambaram Stadium, Chepauk': 4110,
    'Rajiv Gandhi International Stadium, Uppal': 3803,
    'Punjab Cricket Association Stadium, Mohali': 2893,
    'Sawai Mansingh Stadium': 2698,
    'Kingsmead': 1291,
    'Sardar Patel Stadium, Motera': 1110,
    'SuperSport Park': 1024,
    'Brabourne Stadium': 1025,
    'Dr DY Patil Sports Academy': 901,
    'Himachal Pradesh Cricket Association Stadium': 831,
    'New Wanderers Stadium': 741,
    'Punjab Cricket Association IS Bindra Stadium, Mohali': 727,
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium': 651,
    'Dubai International Cricket Stadium': 649,
    "St George's Park": 645,
    'Sheikh Zayed Stadium': 611,
    'Sharjah Cricket Stadium': 559,
    'Newlands': 554,
    'Barabati Stadium': 545,
    'JSCA International Stadium Complex': 534,
    'Shaheed Veer Narayan Singh International Stadium': 459,
    'Maharashtra Cricket Association Stadium': 379,
    'Buffalo Park': 280,
    'Vidarbha Cricket Association Stadium, Jamtha': 276,
    'De Beers Diamond Oval': 275,
    'Holkar Cricket Stadium': 190,
    'OUTsurance Oval': 187,
    'Subrata Roy Sahara Stadium': 91
}
numTeam = len(teams)
for i in range(numTeam):
    a = [0]*numTeam
    a[i] = 1
    teamsHot[teams[i]] = a


def hotTeam(team):
    return teamsHot[team]


def hotVenue(venue):
    return venuesHot[venue]


if __name__ == "__main__":
    print(teamsHot)
