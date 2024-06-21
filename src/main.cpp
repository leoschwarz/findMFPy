#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "base/base/base.h"
#include "base/base/cumsum.h"
#include "base/ms/generatesamplespec.h"
#include "base/ms/peakpickerqtof.h"
#include "base/stats/normal.h"
#include <boost/test/unit_test.hpp>

int add(int i, int j) { return i + j; }

auto pick_peaks(const std::vector<double> &mz_arr,
                const std::vector<double> &int_arr) {
  const double resolution = 10000;
  std::pair<double, double> massrange =
      std::make_pair(mz_arr.front(), mz_arr.back());
  ralab::base::ms::PeakPicker<double, ralab::base::ms::SimplePeakArea> pp(
      resolution, massrange);
  pp(mz_arr.begin(), mz_arr.end(), int_arr.begin());

  return std::make_tuple(pp.getPeakMass(), pp.getPeakArea());
}

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
  m.doc() = R"pbdoc(
      Pybind11 example plugin
      -----------------------
      .. currentmodule:: python_example
      .. autosummary::
         :toctree: _generate
         add
         subtract
  )pbdoc";

  m.def("add", &add, R"pbdoc(
      Add two numbers
      Some other explanation about the add function.
  )pbdoc");

  m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
      Subtract two numbers
      Some other explanation about the subtract function.
  )pbdoc");

  m.def("pick_peaks", &pick_peaks, R"pbdoc(
      Pick peaks from a spectrum
  )pbdoc");
}
