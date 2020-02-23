'''
Created on Feb 17, 2019

@author: Daniel Procopio
@summary: This Class generates a config file from a jinja2 template and a YAML config file.
@version: 1.0
'''
import logging
import pathlib
import yaml
from jinja2 import Environment, FileSystemLoader


class Cfg(object):
    '''
    
    '''
    _CfgYAMLData = ""
    _CfgTemplate = ""
    _CfgOutputFile = ""
    _CfgGenerated = ""
    _Logger = logging.getLogger('jinja2cfg.GeneratedConfig')

    def __init__(self, CfgYAMLData, CfgTemplate, CfgOutputFile=""):
        '''
        YAML data file, Jinja2 Template file are required parameters, output file is optional
        '''
        self._CfgYAMLData = CfgYAMLData
        self._CfgTemplate = CfgTemplate
        self._CfgOutputFile = CfgOutputFile
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s [%(name)-25s] [%(levelname)-8s] - %(message)s',
                            datefmt='%Y-%m-%d %H:%M')

    def generate(self):
        '''
        Generates the config. If no output file is passed, it will store the config into _CfgGenerated variable
        ''' 
        self._Logger.info("Loading config data from "+self._CfgYAMLData)
        config_data = yaml.load(open(self._CfgYAMLData))
        templatePath = str(pathlib.Path(self._CfgTemplate).parent)
        templateFile = pathlib.Path(self._CfgTemplate).name
        self._Logger.info("Loading templates from "+templatePath+" directory")
        env = Environment(loader = FileSystemLoader(templatePath), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template(templateFile)
        if ( self._CfgOutputFile != "" ):
            self._Logger.info("Creating "+self._CfgOutputFile+" config file using "+self._CfgTemplate+" template")
            f = open(self._CfgOutputFile,"w")
            f.write(template.render(config_data))
            f.close()
        else:
            self._Logger.info("Generating config file using "+self._CfgTemplate+" template")
            self._CfgGenerated = template.render(config_data)
        self._Logger.info("Done")
        
    def getGeneratedCfg(self):
        '''
        If no output file is passed, this method can be used to retreive the generated config.
        It returns None in case _CfgGenerated variable is empty 
        '''
        if ( self._CfgGenerated != "" ):
            return self._CfgGenerated
        else:
            return None
