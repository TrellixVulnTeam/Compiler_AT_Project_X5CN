#
# @parameters_java.py Copyright (c) 2020 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 subsuelo Edif. La Unión, Av. Gral. Inofuentes, Calacoto, La Paz, Bolivia
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the termns of the license agreement you entered into
# with Jalasoft.
#

# All java jdk must be directed here
# This path should be changed pointing to the java jdk folder.
JAVA13_PATH = r"C:/Users/acruz/Desktop/ProjectCompiler/Compiler_AT_Project/third_parties/java/jdk-13.0.2/bin"

class ParametersJava:
    def __init__(self):
        self.__path_version = ''
        self.__binary = ''
        self.__package = ''
        self.__mainapp = ''
    
    # Getter Setter Version
    def get_version(self):
        return self.__path_version

    def set_version(self, ver):
        if (ver == 13):
            self.__path_version = JAVA13_PATH

    # Getter Setter Binary
    def get_binary(self):
        return self.__binary

    def set_binary(self, binary):
        self.__binary = binary

    # Getter Setter Package
    def get_package(self):
        return self.__package

    def set_package(self, package):
        self.__package = package

   # Getter Setter MainApp
    def get_main_app(self):
        return self.__mainapp

    def set_main_app(self, mainapp):
        self.__mainapp = mainapp
