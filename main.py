import argparse
import src.logger.logger as log
import src.env_settings as env
import logging
import sys
from src.examen.examen import * 
import os 
s
def save_names(name_files):
    with open('name_files.txt', 'w') as fichero:
        for name in name_files:
            fichero.write('{0}\n'.format(name))


name_files = []

for root, dirs, files in os.walk(".", topdown=False):
    
    for name in files:
        text = name.split('.')
        print(name)
        if 'txt' in name:
            name_files.append(name)


        
print(name_files)
save_names(name_files)

def main():
    #Creating the Enviroment Variables
    
    logger = log.LoggerMaster(log_path="./logs/", 
                              logging_level=logging.DEBUG,
                              log_identifier="testing")
    #Init the logger and first message
    logger.init_logger()
    logger.first_log()
    
    try:
        
        logger.logger.log(logging.INFO, "Starting ")
        
        #Loading the Enviroment Variables
        env_variables = env.LoadEnviroment()
        
        #Creating the Logger Object
        logger = log.LoggerMaster(log_path=env_variables.log_path,
                                  logging_level=env_variables.log_level,
                                  log_identifier=env_variables.log_identifier)
        
        #Init the logger and first message
        logger.init_logger()
        logger.first_log()
    

        #START CODING FROM HERE
        logger.logger.log(logging.INFO, "Starting" +
                           env_variables.log_identifier + "ETL")
        
        #Read csv in dataframe
        Obj = Vehiculo(env_variables, logger)
        Obj.read_data()
        

        
    except Exception as err:
        logger.logger.log(logging.ERROR, "\n Main function Error ({}".format(err) + ")")
        sys.exit(-1)
    
    
    
if __name__ == '__main__':
    main()
