Geoloc = tuple[float, float]
GeoPath = list[Geoloc]
Leg = tuple[Geoloc, Geoloc]

def maritime_distance(
    origin: Geoloc,
    destination: Geoloc,
) -> tuple[float, GeoPath]:
    """
    Calculate the maritime distance in km between two (lat, lng) coordinates
    it uses the haversine formula and the MARNET geograph for determining
    the shortest path and calculating the total distance.

    If no path that connects the two coordinates is found in the geograph,
    then the direct haversine distance between the two points and a path
    only containing the origin and destination points are returned.


    Args:
        origin (Geoloc): The coordinates of the origin point.
        destination (Geoloc): The coordinates of the destination
        point.

    Returns:
        tuple[float, GeoPath]: A tuple containing the maritime distance
        and the path as a Geoloc list, including origin and destination.
    """
    ...

def par_maritime_distance(
    legs: list[Leg],
) -> list[tuple[float, GeoPath]]:
    """
    Calculate the parallel maritime distance for a list of legs. This will
    leverage all available CPU cores to calculate distances.

    Args:
        legs (list[Leg]): A list of Leg objects representing an
        origin/destination pair.

    Returns:
        list[tuple[float, GeoPath]]: A list of tuples, where each tuple
        contains the maritime distance in km and the corresponding
        GeoPath for each leg.

    """
    ...

def highway_distance(
    origin: Geoloc,
    destination: Geoloc,
) -> tuple[float, GeoPath]:
    """
    Calculate the highway distance in km between two (lat, lng) coordinates
    it uses the haversine formula and the MARNET geograph for determining
    the shortest path and calculating the total distance.

    If no path that connects the two coordinates is found in the geograph,
    then the direct haversine distance between the two points and a path
    only containing the origin and destination points are returned.


    Args:
        origin (Geoloc): The coordinates of the origin point.
        destination (Geoloc): The coordinates of the destination
        point.

    Returns:
        tuple[float, GeoPath]: A tuple containing the highway distance
        and the path as a Geoloc list, including origin and destination.
    """
    ...

def par_highway_distance(
    legs: list[Leg],
) -> list[tuple[float, GeoPath]]:
    """
    Calculate the parallel highway distance for a list of legs. This will
    leverage all available CPU cores to calculate distances.

    Args:
        legs (list[Leg]): A list of Leg objects representing an
        origin/destination pair.

    Returns:
        list[tuple[float, GeoPath]]: A list of tuples, where each tuple
        contains the highway distance in km and the corresponding
        GeoPath for each leg.

    """
    ...

def railway_distance(
    origin: Geoloc,
    destination: Geoloc,
) -> tuple[float, GeoPath]:
    """
    Calculate the railway distance in km between two (lat, lng) coordinates
    it uses the haversine formula and the MARNET geograph for determining
    the shortest path and calculating the total distance.

    If no path that connects the two coordinates is found in the geograph,
    then the direct haversine distance between the two points and a path
    only containing the origin and destination points are returned.


    Args:
        origin (Geoloc): The coordinates of the origin point.
        destination (Geoloc): The coordinates of the destination
        point.

    Returns:
        tuple[float, GeoPath]: A tuple containing the railway distance
        and a list of intermediate distances, including origin and destination.
    """
    ...

def par_railway_distance(
    legs: list[Leg],
) -> list[tuple[float, GeoPath]]:
    """
    Calculate the parallel railway distance for a list of legs. This will
    leverage all available CPU cores to calculate distances.

    Args:
        legs (list[Leg]): A list of Leg objects representing an
        origin/destination pair.

    Returns:
        list[tuple[float, GeoPath]]: A list of tuples, where each tuple
        contains the railway distance in km and the corresponding
        GeoPath for each leg.

    """
    ...
