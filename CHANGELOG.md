# Changelog

The format for this changelog is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to (mostly) [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
All dates listed follow the ISO standard of yyyy-mm-dd.

## [v0.2.1] - 2022-10-13
### Added
 - sun_angle now uses numba to improve runtime on repeated calls [David Richardson <drichardson42@gatech.edu>]

## [v0.2.0] - 2022-09-15
### Added
 - mask function to compute boolean array for daytime/nighttime locations [David Richardson <drichardson42@gatech.edu>]
 - easy_mask function to wrap mask with simpler arguments [David Richardson <drichardson42@gatech.edu>]
 - Allow 2D inputs in sun_angle [David Richardson <drichardson42@gatech.edu>]
### Changed
 - Renamed elevation to altitude in sun_angle [David Richardson <drichardson42@gatech.edu>]

## [v0.1.0] - 2022-09-14
### Added
 - julian_day function to compute Julian Day (days since Jan 1, 4713 BC 12 UT) [David Richardson <drichardson42@gatech.edu>]
 - sun_angle function to compute altitude angle at any location and elevation [David Richardson <drichardson42@gatech.edu>]
