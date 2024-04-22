def maritime_distance(
    origin: tuple[float, float],
    destination: tuple[float, float],
) -> tuple[float, list[float]]:
    """
    Calculate the maritime distance in km between two (lat, lng) coordinates
    it uses the haversine formula and the MARNET geograph for determining
    the shortest path and calculating the total distance.

    If no path that connects the two coordinates is found in the geograph,
    then the direct haversine distance between the two points and a path
    only containing the origin and destination points are returned.


    Args:
        origin (tuple[float, float]): The coordinates of the origin point.
        destination (tuple[float, float]): The coordinates of the destination
        point.

    Returns:
        tuple[float, list[float]]: A tuple containing the maritime distance
        and a list of intermediate distances, including origin and destination.
    """
    ...

def highway_distance(
    origin: tuple[float, float],
    destination: tuple[float, float],
) -> tuple[float, list[float]]:
    """
    Calculate the highway distance in km between two (lat, lng) coordinates
    it uses the haversine formula and the MARNET geograph for determining
    the shortest path and calculating the total distance.

    If no path that connects the two coordinates is found in the geograph,
    then the direct haversine distance between the two points and a path
    only containing the origin and destination points are returned.


    Args:
        origin (tuple[float, float]): The coordinates of the origin point.
        destination (tuple[float, float]): The coordinates of the destination
        point.

    Returns:
        tuple[float, list[float]]: A tuple containing the highway distance
        and a list of intermediate distances, including origin and destination.
    """
    ...

def railway_distance(
    origin: tuple[float, float],
    destination: tuple[float, float],
) -> tuple[float, list[float]]:
    """
    Calculate the railway distance in km between two (lat, lng) coordinates
    it uses the haversine formula and the MARNET geograph for determining
    the shortest path and calculating the total distance.

    If no path that connects the two coordinates is found in the geograph,
    then the direct haversine distance between the two points and a path
    only containing the origin and destination points are returned.


    Args:
        origin (tuple[float, float]): The coordinates of the origin point.
        destination (tuple[float, float]): The coordinates of the destination
        point.

    Returns:
        tuple[float, list[float]]: A tuple containing the railway distance
        and a list of intermediate distances, including origin and destination.
    """
    ...
