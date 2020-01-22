# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:29:49 2020

@author: 3decision
"""

from api_python_3decision import settings
from api_python_3decision.session import req_session

from api_python_3decision.endpoints.get_structure import __get_structure__
from api_python_3decision.endpoints.post_structure import __post_structure__
from api_python_3decision.endpoints.get_project_id import __get_project_id__

session = req_session.get_session(settings.params)

def get_structure(code: str):
    return __get_structure__(session, code)
    
def post_structure(archive : str):
    return __post_structure__(session, archive)

def get_project_id(project_name : str):
    return __get_project_id__(session, project_name)
