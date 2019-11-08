# import sys
# from osgeo import ogr

import turtle as t

myList = [0]
firstItem = 0
myList[firstItem]
NAME = 0
POINTS = 1
POP = 2

graphics = []
state = ["Colorado", [[-109, 37], [-109, 41], [-102, 41], [-102, 41], [-102, 37]], 5187582]
cities = (["Denver", [-104.98, 39.74], 634265], ["Boulder", [-105.27, 40.02], 17069], ["Durango", [-107.88, 37.28], 17069])
# cities.append("Denver", [-104.98, 39.74, 634265])
# cities.append("Boulder", [-105.27, 40.02, 17069])
# cities.append("Durango", [-107.88, 37.28, 17069])
# print((cities[POINTS]))

# defining map size
map_width = 400
map_height = 300

# scaling the map (loop through long and lat)
min_x = 180
max_x = -180
min_y = 90
max_y = -90
for x, y in state[POINTS]:
    if x < min_x:
        min_x = x
    elif x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    elif y > max_y:
        max_y = y

    # scaling- coordinate to pixel conversion (calculating ration btn actual state and the tiny canvas renderer)
dist_x = max_x - min_x
dist_y = max_y - min_y
x_ratio = map_width / dist_x
y_ratio = map_height / dist_y


def convert(point):
    lon = point[0]
    lat = point[1]
    x = map_width - ((max_x - lon) * x_ratio)
    y = map_height - ((max_y - lat) * y_ratio)

    # we need to offset the points so that they are centered because turtle start in the middle of the screen

    x = x - (map_width / 2)
    y = y - (map_height / 2)

    return [x, y]


t.up()
first_pixel = None
for point in state[POINTS]:
    pixel = convert(point)
    if not first_pixel:
        first_pixel = pixel
    t.goto(pixel)
    t.down
t.goto(first_pixel)
t.up()
t.goto([0, 0])
t.write(state[NAME], align="center", font=('Arial', 16, "bold"))

# rendering cities

for city in cities:
    pixel = convert(city[POINTS])
    t.up()
    t.goto(pixel)

    # place a point for city
    t.dot(10)
    # label the city
    # POP = str(POP)
t.write(city[NAME] + ", Pop.: " + str(city[POP]), align="left")
output = t.write(city[NAME] + ", Pop.: " + str(city[POP]), align="left")

graphics.append(output)
print(output)

# which city has the largest population?
biggest_city = max(cities, key=lambda city : city[POP])
t.goto(0, 200)
t.write("The biggest city is:" + biggest_city[NAME])

print("The biggest city is:" + biggest_city[NAME])

# which city lies the furthest west?
western_city = min(cities, key=lambda city: city[POINTS])
t.goto(0, -220)
t.write("The Western-most city is:" + western_city[NAME])

print("The Western-most city is:" + western_city[NAME])


simplegis.py