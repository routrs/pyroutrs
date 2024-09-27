# routrs
Geograph-based shortest distance calculation for Python. 100% in Rust.
Based on the [routrs](https://github.com/routrs/routrs) rust crate.

The distance calculation functions in this library are designed to work with various types of geographs (maritime, highway, or railway).

When provided with origin and destination coordinates, the library will attempt to find the nearest points on the respective geograph if the given coordinates are not directly on it.

Distance calculations are performed using the [haversine](https://en.wikipedia.org/wiki/Haversine_formula) formula between nodes in the geograph, ensuring accurate representations of distances on a spherical surface. Then, the shortest path is calculated using the [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).


It's important to note that if no path connecting the two coordinates is found in the geograph, the function will return the direct haversine distance between the two points, along with a path containing only the origin and destination points.

Please be aware that this library is primarily intended for generating realistic distance estimates and paths for visualization or estimation purposes. It is not designed for precise navigation or routing in real-world scenarios. The calculated routes and distances should be used for approximations and visual representations rather than as definitive guidance for actual travel or transportation planning.

## Available Geographs

- **Maritime**: based on the [MARNET](http://marnetproject.eu/) geograph.
- **Highways**: based on the [OpenStreetMap](https://www.openstreetmap.org/) highways database
- **Railways**: based on the [OpenStreetMap](https://www.openstreetmap.org/) railways database

## Installation

```bash
pip install pyroutrs 
# or
poetry install pyroutrs
```

## Usage

```python
from pyroutrs import maritime_distance, Geoloc

origin: Geoloc = (40.6759, -74.0504)
destination: Geoloc = (41.0067858, 28.9732219)

distance, path = maritime_distance(origin, destination)

print(distance) # 9224.95741604269
print(len(path)) # 118
print(path[0]) # (40.6759, -74.0504)
print(path[-1]) # (41.0067858, 28.9732219)

distance, path = highway_distance(origin, destination)

print(distance) # 57.237115955889074
print(len(path)) # 39

distance, path = railway_distance(origin, destination)

print(distance) # 749.4744344461568
print(len(path)) # 603
```

## Parallel Calculations

For bulk distance calculations, you can use the parallel functions. They accept a list of `Leg` objects and return a list of tuples, where each tuple contains the distance and the path.

These parallel functions will leverage all available CPU cores to calculate distances, regardless of the GIL, since the distance calculations are performed in Rust.

```python
from pyroutrs import par_maritime_distance, Leg

legs: list[Leg] = [(origin, destination), (origin, destination)]
distances = par_maritime_distance(legs)

for distance, path in distances:  
    print(distance) # 9224.95741604269
    print(path[0]) # (40.6759, -74.0504)
    print(path[-1]) # (41.0067858, 28.9732219)

```




## Type Annotations

The `Geoloc` type is a `tuple[float, float]` representing a latitude and longitude.

The `GeoPath` type is a `list[Geoloc]` representing a path of coordinates.

The `Leg` type is a `tuple[Geoloc, Geoloc]` representing an origin and destination.

## License

MIT

## Contributing

Contributions are welcome! Please open an issue or submit a PR.
Contact Carlo Casorzo at carlo[a]deepblu.dev or in X [@deepbludev](https://x.com/deepbludev)

## Development

```bash
poetry install

# Build the package
maturin develop --manifest-path Cargo.toml
# or
poe build:dev

# Run the tests
poe test
```

## Attributions
Inspired by [scgraph](https://github.com/connor-makowski/scgraph) and [searoute](https://github.com/genthalili/searoute-py), including the use their datasets, which have been modified to work with this package.



