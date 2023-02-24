E = ["AB", "AC", "AE", "BC", "BE", "CE", "BD", "EG", "ED", "DG", "GH", "DH", "DF", "FH"]
V = set("ABCDEFGH")
weight = [2, 2, 7, 2, 2, 5, 9, 9, 10, 2, 17, 16, 5, 17]
ostov = set("A")
sum = 0

while ostov != V:
    temp_rebra = []
    temp_weight = []
    for i in range(len(E)):
        if (E[i][0] in ostov and E[i][1] not in ostov) or (E[i][1] in ostov and E[i][0] not in ostov):
            temp_rebra.append(E[i])
            temp_weight.append(weight[i])
    for j in range(len(temp_rebra)):
        if temp_weight[j] == min(temp_weight):
            ostov.update(temp_rebra[j])
            sum += temp_weight[j]
            break

print(sum)
