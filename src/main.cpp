#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "base/base/base.h"
#include "base/base/cumsum.h"
#include "base/ms/generatesamplespec.h"
#include "base/ms/peakpickerqtof.h"
#include "base/stats/normal.h"

namespace py = pybind11;
using PeakPicker =
    ralab::base::ms::PeakPicker<double, ralab::base::ms::SimplePeakArea>;

namespace py = pybind11;

auto pick_peaks_generic(const py::array_t<double> &mz_arr,
                        const py::array_t<double> &int_arr,
                        const double resolution, const double width,
                        const double int_width, const double int_threshold,
                        const bool area, const uint32_t max_peaks) {

  std::vector<double> mz_vec(mz_arr.data(), mz_arr.data() + mz_arr.size());
  std::vector<double> int_vec(int_arr.data(), int_arr.data() + int_arr.size());

  std::pair<double, double> massrange =
      std::make_pair(mz_vec.front(), mz_vec.back());
  PeakPicker pp(resolution, massrange, width, int_width, int_threshold, area,
                max_peaks);
  pp(mz_vec.begin(), mz_vec.end(), int_vec.begin());
  return pp;
}

auto pick_peaks(const py::array_t<double> &mz_arr,
                const py::array_t<double> &int_arr, const double resolution,
                const double width, const double int_width,
                const double int_threshold, const bool area,
                const uint32_t max_peaks) {
  auto pp = pick_peaks_generic(mz_arr, int_arr, resolution, width, int_width,
                               int_threshold, area, max_peaks);
  return std::make_tuple(pp.getPeakMass(), pp.getPeakArea());
}

PYBIND11_MODULE(_core, m) {
  m.doc() = R"pbdoc(
      Pybind11 example plugin
      -----------------------
      .. currentmodule:: python_example
      .. autosummary::
         :toctree: _generate
  )pbdoc";

  m.def("pick_peaks", &pick_peaks, R"pbdoc(
      Pick peaks from a spectrum
  )pbdoc");
}
