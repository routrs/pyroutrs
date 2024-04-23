use pyo3::exceptions::PyValueError;
use pyo3::wrap_pyfunction;

pub mod highways;
pub mod maritime;
pub mod railways;

use ::routrs::concurrency::*;
use ::routrs::prelude::*;
use pyo3::prelude::*;

macro_rules! add_distance_function {
    ($rs_distance:expr, $py_distance:ident, $py_module:ident) => {
        #[pyfunction]
        fn $py_distance(origin: Geoloc, destination: Geoloc) -> PyResult<(f64, Vec<Geoloc>)> {
            match $rs_distance(&origin, &destination) {
                Ok((distance, path, _)) => Ok((distance, path.to_vec())),
                Err(e) => Err(PyValueError::new_err(e.to_string())),
            }
        }

        $py_module.add_function(wrap_pyfunction!($py_distance, $py_module)?)?;
    };
}

macro_rules! add_par_distance_function {
    ($rs_par_distance:expr, $py_par_distance:ident, $py_module:ident) => {
        #[pyfunction]
        fn $py_par_distance(legs: Vec<(Geoloc, Geoloc)>) -> PyResult<Vec<(f64, Vec<Geoloc>)>> {
            match $rs_par_distance(
                legs.iter()
                    .map(|(origin, destination)| Leg((*origin, *destination)))
                    .collect::<Vec<_>>()
                    .as_slice(),
            ) {
                Ok(distances) => Ok(distances
                    .into_iter()
                    .map(|(distance, path)| (distance, path.to_vec()))
                    .collect()),
                Err(e) => Err(PyValueError::new_err(e.to_string())),
            }
        }

        $py_module.add_function(wrap_pyfunction!($py_par_distance, $py_module)?)?;
    };
}

#[pymodule]
fn routrs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    add_distance_function!(maritime::distance, maritime_distance, m);
    add_distance_function!(highways::distance, highway_distance, m);
    add_distance_function!(railways::distance, railway_distance, m);

    add_par_distance_function!(maritime::par_distance, par_maritime_distance, m);
    add_par_distance_function!(highways::par_distance, par_highway_distance, m);
    add_par_distance_function!(railways::par_distance, par_railway_distance, m);

    Ok(())
}
