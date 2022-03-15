import os
import sys
import argparse
import logging
import datetime as dt

from fishnet_generator import fishnet_func
from hru_parameters import hru_parameters
from dem_parameters import dem_parameters
from dem_2_streams import flow_parameters
from crt_fill_parameters import crt_fill_parameters
from stream_parameters import stream_parameters
from veg_parameters import veg_parameters
from soil_raster_prep import soil_raster_prep
from soil_parameters import soil_parameters
from prism_800m_normals import prism_800m_parameters
from ppt_ratio_parameters import ppt_ratio_parameters
from impervious_parameters import impervious_parameters
from prms_template_fill import prms_template_fill


def run_batch(overwrite=True):
    args = argparse.Namespace(ini=r'C:\Users\CNA372\gsflow-arcpy-master\uyws_multibasin\uyws_parameters.ini',
                              overwrite=overwrite)
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info('\n{}'.format('#' * 80))
    log_f = '{:<20s} {}'
    logging.info(log_f.format(
        'Run Time Stamp:', dt.datetime.now().isoformat(' ')))
    logging.info(log_f.format('Current Directory:', os.getcwd()))
    logging.info(log_f.format('Script:', os.path.basename(sys.argv[0])))

    logging.info('\n\n\n\nfishnet_func \n\n\n\n')
    fishnet_func(config_path=args.ini, overwrite_flag=args.overwrite)

    logging.info('\n\n\n\nhru_parameters \n\n\n\n')
    hru_parameters(config_path=args.ini)

    logging.info('\n\n\n\ndem_parameters \n\n\n\n')
    dem_parameters(config_path=args.ini)

    logging.info('\n\n\n\nveg_parameters \n\n\n\n')
    veg_parameters(config_path=args.ini)

    logging.info('\n\n\n\nsoil_raster_prep \n\n\n\n')
    soil_raster_prep(config_path=args.ini)

    logging.info('\n\n\n\nsoil_parameters \n\n\n\n')
    soil_parameters(config_path=args.ini)

    logging.info('\n\n\n\nimpervious_parameters \n\n\n\n')
    impervious_parameters(config_path=args.ini)

    logging.info('\n\n\n\nprism_800m_parameters \n\n\n\n')
    prism_800m_parameters(config_path=args.ini)

    logging.info('\n\n\n\nppt_ratio_parameters \n\n\n\n')
    ppt_ratio_parameters(config_path=args.ini)

    logging.info('\n\n\n\nflow_parameters \n\n\n\n')
    flow_parameters(config_path=args.ini)

    logging.info('\n\n\n\ncrt_fill_parameters \n\n\n\n')
    crt_fill_parameters(config_path=args.ini)

    logging.info('\n\n\n\nstream_parameters \n\n\n\n')
    stream_parameters(config_path=args.ini)

    logging.info('\n\n\n\nprms_template_fill \n\n\n\n')
    prms_template_fill(config_path=args.ini)


if __name__ == '__main__':
    run_batch(overwrite=True)
# ========================= EOF ====================================================================
