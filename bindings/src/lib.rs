mod add;
pub mod maritime;

use ::routrs::Geoloc;
use add::add;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn add_numbers(left: usize, right: usize) -> PyResult<usize> {
    Ok(add(left, right))
}

#[pyfunction]
fn maritime_distance(origin: Geoloc, destination: Geoloc) -> PyResult<(f64, Vec<Geoloc>)> {
    match maritime::distance(&origin, &destination) {
        Ok((distance, path)) => Ok((distance, path)),
        Err(e) => Err(PyValueError::new_err(e.to_string())),
    }
}

#[pymodule]
fn routrs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    m.add_function(wrap_pyfunction!(maritime_distance, m)?)?;
    Ok(())
}
