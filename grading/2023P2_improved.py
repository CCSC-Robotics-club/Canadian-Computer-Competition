n = int(input())
_ = input().split()
mounts = []
for i in _:
    mounts.append(int(i))

def mina(length):
    ans = float("inf")
    for bias in range(n - length+1):
        crop = (bias,bias+length-1)
        ans = min(avalue(crop), ans)
    return ans

avalues = dict()
def avalue(crop:set):
    global avalues
    
    left,right = crop[0],crop[1]
    if left >= right:
        return 0
    
    if crop in avalues.keys():
        return avalues[crop]
    ans = abs(mounts[left]-mounts[right])
    ans += avalue((left+1, right-1))
    avalues[crop] = ans
    return ans

answers = [0 for i in range(n)]
for i in range(1, n+1):
   answers[i-1] = mina(i)

for i in answers:
    print(i, end=" ")


