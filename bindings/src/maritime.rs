use routrs::prelude::*;
use routrs::MARITIME;

pub fn distance(origin: &Geoloc, destination: &Geoloc) -> Result<(f64, Vec<Geoloc>), String> {
    let (distance, path, _) = MARITIME.distance(origin, destination)?;
    Ok((distance, path))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_calculates_maritime_distance() {
        let from: Geoloc = (40.6759, -74.0504); // USNYC
        let to: Geoloc = (41.0067858, 28.9732219); // TRIST
        let (distance, path) = distance(&from, &to).unwrap();

        assert_eq!(distance, 9224.95741604269);
        assert_eq!(path.len(), 117);
    }
}
