pub mod maritime;

use ::routrs::prelude::*;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn maritime_distance(origin: Geoloc, destination: Geoloc) -> PyResult<(f64, Vec<Geoloc>)> {
    match maritime::distance(&origin, &destination) {
        Ok((distance, path, _)) => Ok((distance, path.to_vec())),
        Err(e) => Err(PyValueError::new_err(e.to_string())),
    }
}

#[pymodule]
fn routrs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(maritime_distance, m)?)?;
    Ok(())
}
