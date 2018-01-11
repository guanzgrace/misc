import random

a = [40,21,10,5,5,5,4,4,3,3]
b = [43,21,10,5,5,4,3,3,3,3]
c = [20,15,15,15,10,5,5,5,5,5]
d = [33, 7, 4, 5, 6, 7, 8, 9, 10, 11]
e = [1,43,31,5,4,4,3,3,3,3]
f = [44,17,2,8,6,6,5,4,4,4]
g = [61,11,5,5,3,3,3,3,3,3]
h = [1,45,31,5,3,3,3,3,3,3]
i = [1,1,5,25,26,31,3,3,3,2]
j = [1, 27, 22, 17, 6, 7, 8, 2, 5, 5]
k = [39, 18, 12, 8, 6, 5, 4, 3, 3, 2]

def compete(k, j):
    k_score = 0
    j_score = 0
    for i in range(10):
        if strats[j][i] > (i+1) * strats[k][i]:
            j_score = j_score + 1
        if (i+1) * strats[j][i] < strats[k][i]:
            k_score = k_score + 1
    scores[j] = scores[j] + j_score
    scores[k] = scores[k] + k_score
    losses[k] = losses[k] + j_score
    losses[j] = losses[j] + k_score

strats = [a, b, c, d, e, f, g, h, i, j, k]
scores = [0 for s in strats]
losses = [0 for s in strats]

for i in range(len(strats)):
    for j in range(i+1,len(strats)):
        compete(i, j)

print("Strategies:")
print("[a, b, c, d, e, f, g, h, i, j, k]")
print("Districts Won:")
print(scores)
print("Districts Lost:")
print(losses)
