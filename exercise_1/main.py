points_c = ((0, 2), (2, 5), (5, 2), (6, 6), (8, 3))
points_count = len(points_c)
points_d = []

for i in range(points_count):
    points_d.append([])
    for j in range(points_count):
        if points_c[i] != points_c[j]:
            points_d[i].append(((points_c[j][0] - points_c[i][0]) ** 2 + (points_c[j][1] - points_c[i][1]) ** 2) ** 0.5)
        else: points_d[i].append(0)

minroute = 10000

for i1 in range(1, points_count):
    for i2 in range(1, points_count):
        for i3 in range(1, points_count):
            for i4 in range(1, points_count):
                if i1 != i2 and i1 != i3 and i1 != i4 and i2 != i3 and i2 != i4 and i3 != i4 and (points_d[i1][i2] + points_d[i2][i3] + points_d[i3][i4] + points_d[0][i1] + points_d[0][i4]) < minroute:
                    point_1, part_1 = points_c[i1], points_d[0][i1]
                    point_2, part_2 = points_c[i2], part_1 + points_d[i1][i2]
                    point_3, part_3 = points_c[i3], part_2 + points_d[i2][i3]
                    point_4, part_4 = points_c[i4], part_3 + points_d[i3][i4]
                    minroute = part_4 + points_d[0][i4]

print(f'{points_c[0]} -> {point_1}[{part_1}] -> {point_2}[{part_2}] -> {point_3}[{part_3}] -> {point_4}[{part_4}] -> {points_c[0]}[{minroute}] = {minroute}')
