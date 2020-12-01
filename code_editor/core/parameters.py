#
# @parameters.py Copyright (c) 2020 Jalasoft.
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
# Author: Juan S. Ontiveros
# Version: 1.0
#

from abc import ABC

# Super class that defines the minimun parameters
# needed to make a simple compilation of a file


class Parameters(ABC):
    def __init__(self):
        self.__language_path = ''
        self.__file_path = ''

    def get_language_path(self):
        return self.__language_path

    def set_language_path(self, language):
        self.__language_path = language

    def get_file_path(self):
        return self.__file_path

    def set_file_path(self, file_path):
        self.__file_path = file_path
