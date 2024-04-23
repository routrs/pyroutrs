use routrs::concurrency::*;
use routrs::maritime;
use routrs::prelude::*;

pub fn distance(origin: &Geoloc, destination: &Geoloc) -> DistanceResult {
    maritime::distance(origin, destination)
}

pub fn par_distance(legs: &[Leg<Geoloc>]) -> Result<Vec<(f64, Path<Geoloc>)>, String> {
    maritime::geograph()
        .par_distance(legs)
        .into_iter()
        .map(|result| result.map(|(distance, path, _)| (distance, path)))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn geoloc_fixtures() -> (Geoloc, Geoloc) {
        let from: Geoloc = (40.6759, -74.0504); // USNYC
        let to: Geoloc = (41.0067858, 28.9732219); // TRIST
        (from, to)
    }

    #[test]
    fn it_calculates_maritime_distance() {
        let (from, to) = geoloc_fixtures();
        let (distance, path, path_type) = distance(&from, &to).unwrap();

        assert_eq!(distance, 9224.95741604269);
        assert_eq!(path.len(), 118);
        assert_eq!(path_type, PathType::ViaWaypoints);
    }

    #[test]
    fn it_parallel_calculates_maritime_distance() {
        let (from, to) = geoloc_fixtures();
        let (expected_distance, expected_path, _) = distance(&from, &to).unwrap();

        let legs: Vec<_> = (0..100).map(|_| Leg((from, to))).collect();
        let distances = par_distance(&legs).unwrap();

        assert_eq!(distances.len(), legs.len());
        for (distance, path) in distances {
            assert_eq!(distance, expected_distance);
            assert_eq!(path.len(), expected_path.len());
        }
    }
}
