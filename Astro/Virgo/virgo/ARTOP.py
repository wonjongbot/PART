import virgo
import os
import sys
import argparse
import datetime
import shutil
import warnings
import time

parser = argparse.ArgumentParser(description='Amazing Telescope of Peter')

parser.add_argument('-obs',
                    metavar='obs_qtt',
                    type=int,
                    help='quantity of observation')
parser.add_argument('-intvl',
                    metavar='intvl',
                    type=int,
                    help='interval between observation')
parser.add_argument('-rf',
                    metavar='rf',
                    type=float,
                    help='rf gain')
parser.add_argument('-iff',
                    metavar='iff',
                    type=float,
                    help='if gain')
parser.add_argument('-bb',
                    metavar='bb',
                    type=float,
                    help='bb gain')
parser.add_argument('-f',
                    metavar='f',
                    type=float,
                    help='frequency')
parser.add_argument('-b',
                    metavar='b',
                    type=float,
                    help='bandwidth')
parser.add_argument('-c',
                    metavar='c',
                    type=int,
                    help='channel')
parser.add_argument('-t',
                    metavar='t',
                    type=float,
                    help='t_step')
parser.add_argument('-d',
                    metavar='d',
                    type=float,
                    help='duration')

args = parser.parse_args()

input_qtt = args.obs
input_intvl = args.intvl
input_rf = args.rf
input_if = args.iff
input_bb = args.bb
input_f = args.f
input_b = args.b
input_c = args.c
input_t = args.t
input_d = args.d

# Define observation parameters
obs = {
    'dev_args': '',
    'rf_gain': input_rf,
    'if_gain': input_if,
    'bb_gain': input_bb,
    'frequency': input_f,
    'bandwidth': input_b,
    'channels': input_c,
    't_sample': input_t,
    'duration': input_d
}

for x in range (input_qtt):
    
    # Begin data acquisition in 10 sec
    virgo.observe(obs_parameters=obs, obs_file='observation.dat', start_in=0)

    # Analyze data, mitigate RFI and export the data as a FITS file
    virgo.plot(obs_parameters=obs, n=20, m=35, f_rest=1420.4057517667e6,
               obs_file='observation.dat', cal_file='calibration.dat',
               rfi=[1419.2e6, 1419.3e6], waterfall_fits='obs.fits',
               slope_correction=True, plot_file='plot.png')
    

    dt_string = datetime.datetime.now().strftime("%B-%d-%Y_%I-%M-%S-%p")
    shutil.copy2('/home/pi/Astro/Virgo/virgo/plot.png','/home/pi/Astro/Virgo/virgo/img/'+ dt_string +'.png')
    time.sleep(input_intvl)



