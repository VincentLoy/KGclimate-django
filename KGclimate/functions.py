# Round to nearest of either .25 or .75, based on KG data format
def round_coordinate(coordinate):
    absolute = abs(coordinate)
    direction = coordinate / absolute
    if (absolute % 1) < 0.5:
        return int(coordinate) + (0.25 * direction)
    else:
        return int(coordinate) + (0.75 * direction)