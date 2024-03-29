'''
Here is my understanding to this problem.

For each day, we define the following tables:
    1. Subway_route = [station1, station2, station3, ..., stationN] by order at which the train arrives.
    2. Time_subway_arrive[stationID] = the time at which the subway arrives at this station.
    
Now we can draw an important conclusion:
    If we can get (using walways) from start to any stationX in time t <= time_subway_arrive[stationX], we are definately able to get to any station after stationN in t=time_subway_arrive[stationID], including the end.

Based on the conclusion, there are four methods we can get to destination:
    1. start -> walways -> end
    2. start -> subway -> end
    3. start -> subway -> walways -> end
    4. start -> walways -> subway -> walways -> end
NOTE that any other moves that jumps between subway and walways, such as "start -> subway -> walways -> subway -> end" will be completely meaningless.
Because according to the conclusion, it will always take time_subway_arrive[stationID] much time to get to a station by subway.

So we can solve the problem by:
(Preparation)
    1. Using the dijkastra's algorithm, compute station_to_destination_time_walways[stationID] = the time needed to get from a station to stationN, using walkways only.
    2. Using the dijkastra's, compute start_to_station_walkways[stationID] = time needed to get from station0 to stationID, using walways only.
(Solution)
    3. For each day, compute subway_route and time_subway_arrive. 
        NOTE that we don't need to walk through all stations, just swap the two station.
    4. Create a variable called catch_subway_time for the minimum amount of time needed to get on the train.
        For any station i, if start_to_station_walkways[i] <= time_subway_arrive[i], catch_subway_time will be AT MOST time_subway_arrive[i] because we can catch the train at that station.
        NOTE that we don't need to look at all the stations, just look at the stations of which their subway arrival time are beeing swaped
    5. Now it will be very easy to compute the time needed to get from start to destination (we define as time_arrival), based on the travel method we use:
        (1: start -> walways -> end) time_arrival = start_to_station_walkways[0]
        (2: start -> subway -> end) time_arrival = time_subway_arrive[n]
        (3: start -> subway -> walways -> end) or (4: start -> walways -> subway -> walways -> end), we let stationT be the station at which you transfer from subway to walways
            time_arrival = time_subway_arrive[stationT] + station_to_destination_time_walways[stationT]
'''


import sys
# sys.setrecursionlimit(99999) # because who gives a

n, w, d = map(int, input().split())

walways = {}  # stores the walways, walways[stationX] = [station1, station2, ...], stations that stationX connects to
walways_reversed = {} # stores the walways, but reversed, walways_reversed[stationX] = [station1, station2, ...], stations that connects to stationX
for i in range(w): # input the walways
    start, end = map(int, input().split())
    # we change every point to 0~n-1
    start -= 1
    end -= 1
    # add them to the table
    if start in walways:
       walways[start].append(end) 
    else:
       walways[start] = [end]
    if end in walways_reversed:
       walways_reversed[end].append(start)
    else:
       walways_reversed[end] = [start]



# run the dijkastra's to find the time needed to get from a station to stationN, using walkways only

station_to_destination_time_walkways = dict()
for i in range(n-1):
   station_to_destination_time_walkways[i] = float("inf")
station_to_destination_time_walkways[n-1] = 0
visited_stations = set([n-1]) # start from station n
flag = True
while flag:
    flag = False
    for walkway_end in visited_stations:
        for walkway_start in walways_reversed[walkway_end]:
            if station_to_destination_time_walkways[walkway_start] > station_to_destination_time_walkways[walkway_end]+1:
                station_to_destination_time_walkways[walkway_start] = station_to_destination_time_walkways[walkway_end]+1
                flag = True 
                break
    if flag:
      visited_stations.add(walkway_start)

print(station_to_destination_time_walkways)