import argparse
import src.logger.logger as log
import src.env_settings as env
import logging
import sys
from src.examen.examen import * 



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
        
        #Create three different dataframes for each vehicle (C, L, R)
        letter = "C"
        df_Car = Obj.FilterVehiculo(letter)
        Obj_Car = Coche(env_variables, logger, df_Car)
        #print(df_Car)
        letter = "L"
        df_Maritime = Obj.FilterVehiculo(letter)
        Obj_Maritime = Maritimo(env_variables, logger, df_Maritime)
        #print(df_Maritime)
        letter = "R"
        df_Rail = Obj.FilterVehiculo(letter)
        Obj_Rail = Rail(env_variables, logger, df_Rail)
        #print(df_Rail)
        
        #Adding type vehicle column and calculate de price sale wihtout taxes
        Obj_Car.SaleWithoutTax()
        Obj_Maritime.SaleWithoutTax()
        Obj_Rail.SaleWithoutTax()
        
        #Incremento por altura
        Obj_Car.IncrementoAltura()
        Obj_Maritime.IncrementoAltura()
        Obj_Rail.IncrementoAltura()
        
        #Incremento longitud
        Obj_Car.IncrementoLongitud()
        Obj_Maritime.IncrementoLongitud()
        Obj_Rail.IncrementoLongitud()
        
        #Calcular precio final
        Obj_Car.PrecioFinal()
        Obj_Maritime.PrecioFinal()
        Obj_Rail.PrecioFinal()
        
        #Guardar CSV
        name = "Coches.csv"
        Obj_Car.write_data(name)
        name = "Marítimo.csv"
        Obj_Maritime.write_data(name)
        name= "Rail.csv"
        Obj_Rail.write_data(name)
        
        
    except Exception as err:
        logger.logger.log(logging.ERROR, "\n Main function Error ({}".format(err) + ")")
        sys.exit(-1)
    
    
    
if __name__ == '__main__':
    main()
