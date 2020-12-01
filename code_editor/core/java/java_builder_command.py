#
# @java_builder_command.py Copyright (c) 2020 Jalasoft.
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
# Author: Alvaro Cruz, Juan S. Ontiveros
# Version: 1.0
#

from code_editor.core.builder_command import BuilderCommand


# class compiler built, based in params class
from code_editor.core.exceptions.command_exceptions import *
from code_editor.core.java.java_parameters import JavaParameters


class JavaBuilderCommand(BuilderCommand):
    def command(self, params):

        cmd = [params.get_language_path() / "javac", "-d", params.get_binary(), params.get_package(),
               "&&", params.get_language_path() / "java", "-cp", params.get_binary(), params.get_file_path()]

        if params.get_language_path() is None:
            raise NoneCommandException(params.get_language_path())
        elif params.get_file_path() is None:
            raise NoneCommandException(params.get_file_path())
        elif params.get_language_path() == '':
            raise EmptyCommandException(params.get_language_path())
        elif params.get_file_path() == '':
            raise EmptyCommandException(params.get_file_path())
        elif not isinstance(params, JavaParameters):
            raise TypeCommandException(params)
        return cmd
