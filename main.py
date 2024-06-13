Points = [(1, 2), (7, 4), (5, 9), (7, 1), (9, 21)]

distances = []

def euclideanDistance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

for i in range(len(Points)):
    for j in range(i + 1,len(Points)):
        x1, y1 = Points[i]
        x2, y2 = Points[j]

        distance = euclideanDistance(x1,y1,x2,y2)
        distances.append(distance)



min_distance = min(distances)

print(distances)

print("Noktalar arasındaki minimum Öklid mesafesi:", min_distance)




