# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:29:49 2020

@author: 3decision
"""

import api_python_3decision.settings as settings
import api_python_3decision.session.req_session as req_session
import api_python_3decision.endpoints as e


session = req_session.get_session(settings.params)

# Structure Endpoints

def get_structure_metadata(code: str):
    return e.structure_endpoints.__get_structure_metadata__(session, code)

def get_structure_ligands(code: str):
    return e.structure_endpoints.__get_structure_ligands__(session, code)
    
def post_structure(archive : str):
    return e.structure_endpoints.__post_structure__(session, archive)


# Project Endpoints

def get_project_ids(project_name : str):
    return e.project_endpoints.__get_project_ids__(session, project_name)


# Ligand Endpoints

def get_ligand_search(search_type: str, input_type : str, input_value : str):
    return e.ligand_endpoints.__ligand_search__(session, search_type, input_type, input_value)
