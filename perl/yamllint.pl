#!/usr/bin/env perl

use YAML::XS;
local $/;
print Dump Load <>;
