use pyo3::exceptions::PyValueError;
use pyo3::wrap_pyfunction;

pub mod highways;
pub mod maritime;
pub mod railways;

use ::routrs::prelude::*;
use pyo3::prelude::*;

macro_rules! add_distance_function {
    ($module_distance:expr, $function:ident, $module_name:ident) => {
        #[pyfunction]
        fn $function(origin: Geoloc, destination: Geoloc) -> PyResult<(f64, Vec<Geoloc>)> {
            match $module_distance(&origin, &destination) {
                Ok((distance, path, _)) => Ok((distance, path.to_vec())),
                Err(e) => Err(PyValueError::new_err(e.to_string())),
            }
        }

        $module_name.add_function(wrap_pyfunction!($function, $module_name)?)?;
    };
}

#[pymodule]
fn routrs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    add_distance_function!(maritime::distance, maritime_distance, m);
    add_distance_function!(highways::distance, highway_distance, m);
    add_distance_function!(railways::distance, railway_distance, m);
    Ok(())
}
