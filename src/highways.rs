use routrs::concurrency::*;
use routrs::highways;
use routrs::prelude::*;

pub fn distance(origin: &Geoloc, destination: &Geoloc) -> ShortestPath {
    highways::shortest_path(origin, destination)
}

pub fn par_distance(legs: &[Leg<Geoloc>]) -> Vec<(f64, Path<Geoloc>)> {
    highways::geograph()
        .par_distance(legs)
        .into_iter()
        .map(|(distance, path, _)| (distance, path))
        .collect()
}
#[cfg(test)]
mod tests {
    use super::*;

    fn geoloc_fixtures() -> (Geoloc, Geoloc) {
        let from: Geoloc = (31.33068357, 120.902694); // Kunshan, Suzhou, Jiangsu, China
        let to: Geoloc = (31.05287995, 121.2232226); // Songjiang District, Shanghai, China
        (from, to)
    }

    #[test]
    fn it_calculates_highway_distance() {
        let (from, to) = geoloc_fixtures();
        let (distance, path, path_type) = distance(&from, &to);

        assert_eq!(distance, 57.237115955889074);
        assert_eq!(path.len(), 39);
        assert_eq!(path_type, PathType::ViaWaypoints);
    }

    #[test]
    fn it_parallel_calculates_highway_distance() {
        let (from, to) = geoloc_fixtures();
        let (expected_distance, expected_path, _) = distance(&from, &to);

        let legs: Vec<_> = (0..100).map(|_| Leg((from, to))).collect();
        let distances = par_distance(&legs);

        assert_eq!(distances.len(), legs.len());
        for (distance, path) in distances {
            assert_eq!(distance, expected_distance);
            assert_eq!(path.len(), expected_path.len());
        }
    }
}
