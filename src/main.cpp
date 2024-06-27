#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "base/base/base.h"
#include "base/base/cumsum.h"
#include "base/ms/generatesamplespec.h"
#include "base/ms/peakpickerqtof.h"
#include "base/stats/normal.h"
// #include <boost/test/unit_test.hpp>

// int add(int i, int j) { return i + j; }

namespace py = pybind11;

auto pick_peaks(const std::vector<double> &mz_arr,
                const std::vector<double> &int_arr,
                const double resolution = 10000, const double width = 2.0,
                const double int_width = 2.0, const double int_threshold = 10.0,
                const bool area = true, const uint32_t max_peaks = 0) {
  std::pair<double, double> massrange =
      std::make_pair(mz_arr.front(), mz_arr.back());
  ralab::base::ms::PeakPicker<double, ralab::base::ms::SimplePeakArea> pp(
      resolution, massrange, width, int_width, int_threshold, area, max_peaks);
  pp(mz_arr.begin(), mz_arr.end(), int_arr.begin());

  return std::make_tuple(pp.getPeakMass(), pp.getPeakArea());
}

auto pick_peaks_np(const py::array_t<double> &mz_arr,
                   const py::array_t<double> &int_arr,
                   const double resolution = 10000, const double width = 2.0,
                   const double int_width = 2.0,
                   const double int_threshold = 10.0, const bool area = true,
                   const uint32_t max_peaks = 0) {
  std::vector<double> mz_vec(mz_arr.data(), mz_arr.data() + mz_arr.size());
  std::vector<double> int_vec(int_arr.data(), int_arr.data() + int_arr.size());

  return pick_peaks(mz_vec, int_vec, resolution, width, int_width,
                    int_threshold, area, max_peaks);
}

PYBIND11_MODULE(_core, m) {
  m.doc() = R"pbdoc(
      Pybind11 example plugin
      -----------------------
      .. currentmodule:: python_example
      .. autosummary::
         :toctree: _generate
  )pbdoc";

  /* keeping these around as example for now
    m.def("add", &add, R"pbdoc(
        Add two numbers
        Some other explanation about the add function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers
        Some other explanation about the subtract function.
    )pbdoc");
  */

  m.def("pick_peaks", &pick_peaks_np, R"pbdoc(
      Pick peaks from a spectrum
  )pbdoc");
}
