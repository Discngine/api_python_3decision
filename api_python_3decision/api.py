# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:29:49 2020

@author: 3decision
"""

import api_python_3decision.settings as settings
import api_python_3decision.session.req_session as req_session
import api_python_3decision.endpoints as e

default_session = req_session.get_session(settings.params)

# Session 
def create_session():
    return req_session.get_session(settings.params)

# Structure Endpoints

def get_structure(code: str, session = default_session):
    return e.structure_endpoints._get_structure(session, code)

def get_structure_metadata(code: str, session = default_session):
    return e.structure_endpoints._get_structure_metadata(session, code)

def get_structure_ligands(code: str, session = default_session):
    return e.structure_endpoints._get_structure_ligands(session, code)

def reanalyze_structure(code: str, session = default_session):
    return e.structure_endpoints._put_reanalyze_structure(session, code)

def post_structure(archive : str, session = default_session):
    return e.structure_endpoints._post_structure(session, archive)

def delete_structure(code : str, session = default_session):
    return e.structure_endpoints._delete_structure(session, code)

def search_structure_annotation(annotation_type: str, annotation_value : str, session = default_session):
    return e.structure_endpoints._search_structure_by_anotation(session, annotation_type, annotation_value)


# Project Endpoints

def get_project_ids(project_name : str, session = default_session):
    return e.project_endpoints._get_project_ids(session, project_name)

def get_project(project_id : int, session = default_session):
    return e.project_endpoints._get_project(session, project_id)
    

# Ligand Endpoints

def get_ligand_search(search_type: str, input_type : str, input_value : str, session = default_session):
    return e.ligand_endpoints._ligand_search(session, search_type, input_type, input_value)

# Annotation Endpoints

def post_biomolecule_annotation(data: str, session = default_session):
    return e.annotation_endpoints._post_biomolecule_annotation(session,data)