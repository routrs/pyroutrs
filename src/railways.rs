use routrs::concurrency::*;

use routrs::prelude::*;
use routrs::railways;

pub fn distance(origin: &Geoloc, destination: &Geoloc) -> DistanceResult {
    railways::distance(origin, destination)
}

pub fn par_distance(legs: &[Leg<Geoloc>]) -> Result<Vec<(f64, Path<Geoloc>)>, String> {
    railways::geograph()
        .par_distance(legs)
        .into_iter()
        .map(|result| result.map(|(distance, path, _)| (distance, path)))
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn geoloc_fixtures() -> (Geoloc, Geoloc) {
        let from: Geoloc = (48.8768, 2.3592); // Gare de l'Est, Paris, France
        let to: Geoloc = (43.3032, 5.3842); // Gare de Marseille-Saint-Charles, Marseille, France
        (from, to)
    }

    #[test]
    fn it_calculates_railway_distance() {
        let (from, to) = geoloc_fixtures();
        let (distance, path, path_type) = railways::distance(&from, &to).unwrap();

        assert_eq!(distance, 749.4744344461568);
        assert_eq!(path.len(), 603);
        assert_eq!(path_type, PathType::ViaWaypoints);
    }

    #[test]
    fn it_parallel_calculates_railway_distance() {
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
