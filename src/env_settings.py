import configparser
import platform
import logging
import sys

class LoadEnviroment:
    def __init__(self):
        try:
            self.config = None
            
            if platform.system()=="Darwin":
                print("[INFO] Running the ELT from Linux System")
                root_dir = "./config"
                config_file = root_dir + "/config.ini"
                
            else:
                print("[INFO] Runing the ELT from Windows System")
                root_dir = ".\\config"
                config_file = root_dir + "\\config_win.ini"
                
            self.config = configparser.ConfigParser()
            self.config.sections()
            self.config.read(config_file)
            
            #logger configuration
            self.log_path = self.config['LOGGING']['LOG_PATH']
            self.log_level = self.config['LOGGING']['LOG_LEVEL']
            
            if self.log_level == 'logging.DEBUG':
                self.log_level = logging.DEBUG
                
            self.log_identifier = self.config['LOGGING']['LOG_IDENTIFIER']
            
            #Reading TEXT configuration
            #self.file_name = self.config['FILE_MANAGEMENT']['FILE_NAME']
            #self.relative_path = self.config['FILE_MANAGEMENT']['RELATIVE_PATH']
            #self.output_name = self.config['FILE_MANAGEMENT']['OUTPUT_FILE_NAME']
            #self.operation = self.config['FILE_MANAGEMENT']['OPERATION']
            
            # Reading CSV configuration
            self.file_name = self.config['CSV_FILE_MANGAMENT']['FILE_NAME']
            self.relative_path = self.config['CSV_FILE_MANGAMENT']['RELATIVE_PATH']
            self.output_file = self.config['CSV_FILE_MANGAMENT']['OUTPUT_FILE_NAME']
            
            #Management JSON configuration
            #self.file_name = self.config['JSON_MANAGEMENT']['FILE_NAME']
            #self.relative_path = self.config['JSON_MANAGEMENT']['RELATIVE_PATH']
            #self.operation = self.config['JSON_MANAGEMENT']['OPERATION']
            #self.output_file = self.config['JSON_MANAGEMENT']['OUTPUT_FILE_NAME']
                        
        except Exception as err:
            print("\n apply_column_mapping function Error ({}".format(err) + ")")
            sys.exit(-1)
            
            