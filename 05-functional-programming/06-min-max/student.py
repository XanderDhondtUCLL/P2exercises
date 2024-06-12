def closest(points, target_point):
    def pythagoras(point):
        x_distance = point[0] - target_point[0]
        y_distance = point[1] - target_point[1]
        return x_distance**2 + y_distance**2
    return min(points, key=pythagoras)