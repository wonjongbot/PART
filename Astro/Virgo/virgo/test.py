import os
import sys
import argparse
import time
import numpy as np
import datetime
import shutil
import warnings
import virgo

# Define observation parameters
obs = {
    'dev_args': '',
    'rf_gain': 60,
    'if_gain': 30,
    'bb_gain': 30,
    'frequency': 1420e6,
    'bandwidth': 2.4e6,
    'channels': 2048,
    't_sample': 1,
    'duration': 30
}


# Check source position
#virgo.predict(lat=39.83, lon=-74.87, source='Cas A', date='2020-12-26')

# Begin data acquisition in 10 sec
virgo.observe(obs_parameters=obs, obs_file='observation.dat', start_in=10)

# Analyze data, mitigate RFI and export the data as a FITS file
virgo.plot(obs_parameters=obs, n=20, m=35, f_rest=1420.4057517667e6,
           obs_file='observation.dat', cal_file='calibration.dat',
           rfi=[1419.2e6, 1419.3e6], waterfall_fits='obs.fits',
           slope_correction=True, plot_file='plot.png')