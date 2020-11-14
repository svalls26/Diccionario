import sys 
import pandas as pd
import logging

class Vehiculo:

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
            
            
    def IncrementoAltura(self):
        """Calcular el Incremento altura"""
        try: 
            self.logger.logger.log(logging.INFO, "IncrementoAltura function") 
            index = 2
            #print(index)
            self.dataframe['Porcentaje_Altura'] = self.dataframe['Altura'].apply(lambda x: 10 if x<=index else 15)
            self.dataframe['Incremento_altura'] = self.dataframe['Precio2']/self.dataframe['Porcentaje_Altura']
            #self.dataframe["Incremento_Altura"] = self.dataframe['Precio']/self.dataframe["Incremento_Altura"]
            print(self.dataframe)                    
        
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error IncrementoAltura function ({}".format(err) + ")")
            sys.exit(-1)
            
    def IncrementoLongitud(self):
        """Calcular el Incremento longitud"""
        try: 
            self.logger.logger.log(logging.INFO, "IncrementoLongitud function") 
            index = 4
            #print(index)
            #self.dataframe.loc[(self.dataframe['Largo'] >4), 'Porcentaje_longitud' ] = 15
            self.dataframe['Porcentaje_longitud'] = self.dataframe['Largo'].apply(lambda x: 15 if x>=index else 1)
            self.dataframe['Incremento_longitud'] = self.dataframe['Precio2']/self.dataframe['Porcentaje_Longitud']
            print(self.dataframe)                    
        
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error IncremenLongitud function ({}".format(err) + ")")
            sys.exit(-1)
            
    def PrecioFinal(self):
        """Calcular el Incremento altura"""
        try: 
            self.logger.logger.log(logging.INFO, "IncrementoAltura function") 
            self.dataframe['Precio_final'] = self.dataframe['Precio'] + self.dataframe['Incremento_tipo'] + self.dataframe['Incremento_altura'] + self.dataframe['Incremento_longitud']
                
        
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error IncrementoAltura function ({}".format(err) + ")")
            sys.exit(-1)            


    def write_data(self, name):
        """Saving DataFrame to a CSV file"""
        try:
            self.logger.logger.log(logging.INFO, "Write_data function") 
            #print(self.dataframe)
            self.dataframe.to_csv(self.__path+self.__output + "_" + name, sep = "\t")

        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error write_data function ({}".format(err) + ")")
            sys.exit(-1)  

class Coche(Vehiculo):
    
    def __init__(self, env_paths, logger, df_Car):
        super().__init__(env_paths, logger, df_Car)
        
    def SaleWithoutTax(self):
        """Calculate sale price without taxes"""
        try: 
            self.logger.logger.log(logging.INFO, "SaleWithoutTax_Car") 
            type_v = "Coche"
            self.dataframe['Tipo'] = type_v
            percentage = 10
            self.dataframe['Incremento_tipo_porcentaje'] = percentage
            self.dataframe['Incremento_tipo'] = self.dataframe['Precio2']/self.dataframe['Incremento_tipo_porcentaje']
            print(self.dataframe)
            #self.dataframe['Precio'] = self.dataframe['Precio'].astype(float)
            #self.dataframe['Incremento_tipo'] = self.dataframe['Precio'] / self.dataframe['Incremento_tipo_porcentaje']
            #print(self.dataframe.dtypes)
                           
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error SaleWithoutTax_Car function ({}".format(err) + ")")
            sys.exit(-1)
        
class Maritimo(Vehiculo):
    def __init__(self, env_paths, logger, df_Maritime):
        super().__init__(env_paths, logger, df_Maritime)
        
    def SaleWithoutTax(self):
        """Calculate sale price without taxes"""
        try: 
            self.logger.logger.log(logging.INFO, "SaleWithoutTax_Maritime") 
            type_v = "Maritimo"
            self.dataframe['Tipo'] = type_v
            percentage = 15
            self.dataframe['Incremento_tipo_porcentaje'] = percentage
            self.dataframe['Incremento_tipo'] = self.dataframe['Precio2']/self.dataframe['Incremento_tipo_porcentaje']
            print(self.dataframe)
                           
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error SaleWithoutTax_Maritime function ({}".format(err) + ")")
            sys.exit(-1)
        
class Rail(Vehiculo):
    def __init__(self, env_paths, logger, df_Rail):
        super().__init__(env_paths, logger, df_Rail)

    def SaleWithoutTax(self):
        """Calculate sale price without taxes"""
        try: 
            self.logger.logger.log(logging.INFO, "SaleWithoutTax_Rail") 
            type_v = "Rail"
            self.dataframe['Tipo'] = type_v
            percentage = 30
            self.dataframe['Incremento_tipo_porcentaje'] = percentage
            self.dataframe['Incremento_tipo'] = self.dataframe['Precio2']/self.dataframe['Incremento_tipo_porcentaje']
            #self.dataframe['Incremento_tipo'] = self.dataframe['Precio"'].divide(self.dataframe['Incremento_tipo_porcentaje'], fill_value=1)
            #self.dataframe["Precio"] = pd.to_numeric(self.dataframe["Precio"])
            #self.dataframe['Incremento_tipo'] = self.dataframe['Precio'] 
            #self.dataframe['Incremento_tipo'] = self.dataframe['Precio'] * 1.3
            print(self.dataframe)
                           
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error SaleWithoutTax_Rail function ({}".format(err) + ")")
            sys.exit(-1)
