mod add;
use add::add;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn add_numbers(left: usize, right: usize) -> PyResult<usize> {
    Ok(add(left, right))
}

#[pymodule]
fn routrs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    Ok(())
}
