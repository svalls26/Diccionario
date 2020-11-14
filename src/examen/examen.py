import sys 
import pandas as pd
import logging

class nombreArchivos:

    def __init__(self, enviroments, logger, dataframe=None):
        """
        This is the class constructor
        """
        self.__file = enviroments.file_name
        self.__path = enviroments.relative_path
        self.__output = enviroments.output_file
        self.logger = logger
        self.dataframe = dataframe
    
    def read_data(self):
        """Read the csv and create a dataframe with those data"""
        try: 
            self.logger.logger.log(logging.INFO, "Reading CSV File using Pandas")
            self.dataframe = pd.read_csv(self.__path+self.__file, sep=";")
            print(self.dataframe.dtypes)
            self.number_rows = len(self.dataframe.index)
            #print(self.number_rows)
            
            
        
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error read_data function ({}".format(err) + ")")
            sys.exit(-1)

    def FilterVehiculo(self, letter):
        """Filter evehicles by type"""
        try: 
            self.logger.logger.log(logging.INFO, "FilterVehicle function") 
            self.df_letter = self.dataframe[self.dataframe['Tipo_Vehiculo'] == letter]

            return self.df_letter
        
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error FilterVehicle function ({}".format(err) + ")")
            sys.exit(-1)
            
            
