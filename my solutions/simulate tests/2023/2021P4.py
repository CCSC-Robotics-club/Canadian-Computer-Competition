n, w, d = map(int, input().split())

connection = {}
for i in range(w):
    a, b = map(int, input().split())
    start = min(a,b)-1
    end = max(a,b)-1
    try:
        connection[start].append(end)  # we change every point to 0~n-1
    except KeyError:
        connection[start] = [end]

time_arrival_results = [[-1 for i in range(n)] for j in range(n)] #[pos, t] = time_arrival
def time_arrival(pos, t):
    if pos == n:
        return t
    if t > n:
        return n # the maximum amount of time needed
    if time_arrival[pos][t]