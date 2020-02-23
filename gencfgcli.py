'''
Created on Feb 17, 2019
@author: Daniel Procopio
@summary: This program invokes the class that generates a config file from a jinja2 template and a YAML config file.
@version: 1.0
'''

import argparse
from   jinja2cfg import config
import logging
import sys


def generateconfig(args):
    newconfig = config.Cfg(args.input_yaml,args.input_template, args.output_file)
    newconfig.generate()
    logger.info(newconfig.getGeneratedCfg())
    logger.info("Done")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(name)-9s] [%(levelname)-8s] - %(message)s',
                        datefmt='%Y-%m-%d %H:%M')
    logger = logging.getLogger('gencfgcli')
        
    main_parser = subparsers.add_parser('gencfg')
    main_parser.add_argument('input_yaml',help='YAML file contaning the configuraton data')
    main_parser.add_argument('input_template',help='Jinja2 template file')
    main_parser.add_argument('output_file',help='Generated config file',default="")
    main_parser.set_defaults(func=generateconfig)

    args = parser.parse_args()
    if len(sys.argv) > 1:
        args.func(args)
    else:
        logger.critical("Missing arguments")
        main_parser.print_help()   
