# Copyright 2016-2019 Markus Scheidgen, Markus Kühbach
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys
import os.path
import json
import ase
import re
import numpy as np
from datetime import datetime

from nomadcore.simple_parser import SimpleMatcher
from nomadcore.baseclasses import ParserInterface, AbstractBaseParser

from nomad.parsing import LocalBackend


class APTFIMParserInterface(ParserInterface):
    def get_metainfo_filename(self):
        """
        The parser specific metainfo. To include other metadata definitions, use
        the 'dependencies' key to refer to other local nomadmetainfo.json files or
        to nomadmetainfo.json files that are part of the general nomad-meta-info
        submodule (i.e. ``dependencies/nomad-meta-info``).
         """
        return os.path.join(os.path.dirname(__file__), 'aptfim.nomadmetainfo.json')

    def get_parser_info(self):
        """ Basic info about parser used in archive data and logs. """
        return {
            'name': 'aptfimparser',
            'version': '0.1.0'
        }

    def setup_version(self):
        """ Can be used to call :func:`setup_main_parser` differently for different code versions. """
        self.setup_main_parser(None)

    def setup_main_parser(self, _):
        """ Setup the actual parser (behind this interface) """
        self.main_parser = APTFIMParser(self.parser_context)


class APTFIMParser(AbstractBaseParser):

    def parse(self, filepath):
        backend = self.parser_context.super_backend

        with open(filepath, 'rt') as f:
            data = json.load(f)
            #print(data)

        # # You need to open sections before you can add values or sub sections to it.
        # # The returned 'gid' can be used to reference a specific section if multiple
        # # sections of the same type are opened.
        #test_gid = backend.openSection('experiment_cantext')
        #backend.addValue('context_headxx', data.get('experiment_type'))
        #backend.closeSection('experiment_context', test_gid)

        root_gid = backend.openSection('section_experiment')
        # # Values do not necessarily have to be read from the parsed file.
        # # The backend will check the type of the given value agains the metadata definition.
        # backend.addValue('experiment_time', int(datetime.strptime(data.get('date'), '%d.%M.%Y').timestamp()))
        #
        # # Read data .
#        data_gid = backend.openSection('section_context')
        #data_gid = backend.openSection('section_experiment')
        # addValue
        # first argument STRING IDENTIFIER IN OUTPUT JSON KEYWORDS from aptfim.nomadmetainfo.json (ie. the generated parser result JSON)
        # second argument STRING IDENTIFIER IN INPUT JSON (ie. the small META DATA FILE TO THE DATASET
        #backend.addValue('data_repository_name', data.get('data_repository_name'))
        #backend.addValue('data_repository_url', data.get('data_repository_url'))
        #backend.addValue('data_preview_url', data.get('data_preview_url'))
#        backend.addValue('real_one', data.get('experiment_typpe'))
#        backend.closeSection('section_context', data_gid)

        # Read general tool environment details
        # general_gid = backend.openSection('section_experiment_general_parameters')
        
        backend.addValue('experiment_method', data.get('experiment_method'))
        backend.addValue('experiment_location', data.get('experiment_location'))
        backend.addValue('experiment_facility_institution', data.get('experiment_facility_institution'))
        backend.addValue('experiment_tool_info', data.get('instrument_info')) ###test here the case that input.json keyword is different to output.json
        
#        backend.addValue('experiment_data_global_start', np.array(re.findall(r"[\w']+", data.get('experiment_data_global_start'))))  ####
#        backend.addValue('experiment_data_global_end', np.array(re.findall(r"[\w']+", data.get('experiment_data_global_end'))))  ####
#        backend.addValue('experiment_data_local_start', np.array(re.findall(r"[\w']+", data.get('experiment_data_local_start')))) ####
        
#        backend.addValue('experiment_operation_method', data.get('experiment_operation_method'))
#        backend.addValue('experiment_imaging_method', data.get('experiment_imaging_method'))

        # Read parameters related to sample
#        backend.addValue('specimen_description', data.get('specimen_description'))
#        backend.addValue('specimen_microstructure', data.get('specimen_microstructure'))
#        backend.addValue('specimen_constitution', data.get('specimen_constitution'))
        
        #### parse chemical composition
        
        ### measured_pulse_voltage for instance should be a conditional read
#        backend.addValue('measured_number_ions_evaporated', data.get('measured_number_ions_evaporated'))
#        backend.addValue('measured_detector_hit_pos', data.get('measured_detector_hit_pos'))
#        backend.addValue('measured_detector_hit_mult', data.get('measured_detector_hit_mult'))
#        backend.addValue('measured_detector_dead_pulses', data.get('measured_detector_dead_pulses'))
#       backend.addValue('measured_time_of_flight', data.get('measured_time_of_flight'))
#        backend.addValue('measured_standing_voltage', data.get('measured_standing_voltage'))
#        backend.addValue('measured_pulse_voltage', data.get('measured_pulse_voltage'))

        
        # To add arrays (vectors, matrices, etc.) use addArrayValues and provide a
        # numpy array. The shape of the numpy array must match the shape defined in
        # the respective metadata definition.


        # Close sections in the reverse order
        #backend.closeSection('section_experiment', data_gid)
        #backend.closeSection('section_data', data_gid)
        backend.closeSection('section_experiment', root_gid)
        # backend.closeSection('section_experiment_general_parameters', general_gid)
        # backend.closeSection('section_experiment_source_parameters', source_gid)
        # backend.closeSection('section_experiment_detector_parameters', detector_gid)
        # backend.closeSection('section_experiment_sample_parameters', sample_gid)
