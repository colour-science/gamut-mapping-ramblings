#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import colour
from colour import read_LUT, write_LUT, LUT3D, LUT3x1D, LUTSequence
from colour.models import RGB_to_RGB, BT2020_COLOURSPACE, P3_D65_COLOURSPACE, eotf_inverse_sRGB
from colour.utilities import tstack

Log2_48_nits_Shaper_to_linear = read_LUT(
    '/Library/Application Support/OpenColorIO/aces_1.1/luts/Log2_48_nits_Shaper_to_linear.spi1d'
)
bt2020_cube = read_LUT(
    '/Library/Application Support/OpenColorIO/aces_1.1/luts/Log2_48_nits_Shaper.RRT.Rec.2020__P3D65_Limited_.spi3d'
)

table = bt2020_cube.table**2.4
table = RGB_to_RGB(table, BT2020_COLOURSPACE, P3_D65_COLOURSPACE)
table = eotf_inverse_sRGB(table)
table = np.clip(table, 0, 1)

display_p3_cube = LUT3D(table=table)

samples = np.linspace(0, 1, 4096)

domain = tstack(
    (Log2_48_nits_Shaper_to_linear.table, Log2_48_nits_Shaper_to_linear.table,
     Log2_48_nits_Shaper_to_linear.table))

shaper = LUT3x1D(domain=domain, table=tstack([samples, samples, samples]))

LUT = LUTSequence(shaper, display_p3_cube)

write_LUT(LUT, '../luts/ACES2065-1_display_P3_OT.csp')
