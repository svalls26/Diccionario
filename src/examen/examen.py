import sys 
import pandas as pd
import logging
import os 

class nombreArchivos:

    def __init__(self, enviroments, logger, name_files):
        """
        This is the class constructor
        """
        self.__nameFiles = name_files
        self.__path = enviroments.relative_path
        self.__output = enviroments.output_name
        self.logger = logger
    
    def SaveNames(self):
        try:
            with open(self.__path+self.__output, 'w') as fichero:
                for name in self.__nameFiles:
                    fichero.write('{0}\n'.format(name))
                    #print(self.number_rows)
    
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error SaveNames function ({}".format(err) + ")")
            sys.exit(-1)

    def SearchNames(self):
        """Filter evehicles by type"""
        try:           
            for root, dirs, files in os.walk(".", topdown=False):
                
                for name in files:
                    text = name.split('.')
                    print(text)
                    if len(text)>=2:
                        if text[1] == "txt":
                            self.__nameFiles.append(name)
                        
            print(self.__nameFiles)
            self.__nameFiles.remove('requirements.txt')
            #self.__nameFiles.remove('file_names.txt')

            return self.__nameFiles
        
        except Exception as err:
            self.logger.logger.log(logging.ERROR, "Error SearchNames function ({}".format(err) + ")")
            sys.exit(-1)
            
            
