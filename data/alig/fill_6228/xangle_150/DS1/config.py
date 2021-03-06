import sys 
import os
import FWCore.ParameterSet.Config as cms

sys.path.append(os.path.relpath("./"))
sys.path.append(os.path.relpath("../../../../../"))

from config_base import config
from input_files import input_files

config.input_files = input_files

config.aligned = True

config.sector_45.cut_h_c = 0

config.sector_45.cut_v_a = -1.07
config.sector_45.cut_v_c = 0.28

config.sector_56.cut_h_c = 0.08

config.sector_56.cut_v_a = -1.07
config.sector_56.cut_v_c = 0.18

config.matching_1d.rp_L_2_F.x_min = 3
config.matching_1d.rp_L_2_F.x_max = 15

config.matching_1d.rp_L_1_F.x_min = 3
config.matching_1d.rp_L_1_F.x_max = 15

config.matching_1d.rp_R_1_F.x_min = 2
config.matching_1d.rp_R_1_F.x_max = 14

config.matching_1d.rp_R_2_F.x_min = 2
config.matching_1d.rp_R_2_F.x_max = 14
