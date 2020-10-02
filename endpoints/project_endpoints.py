# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:53:17 2020

@author: 3decision
"""

def _get_project_ids(session, project_name : str):
    session.check_token_expiration()
    get_project_id_endpoint = '/project/:name/ids'
    url = session.api_base_url + get_project_id_endpoint
    url = url.replace(':name', project_name)
    response = session.req.get(url)
    if response.status_code > 202:
        session.print_error_message(response)
    return response

def _get_project(session, project_id : int):
    session.check_token_expiration()
    get_project_id_endpoint = '/project/:id?metadataType=general, users, structures, customTransformations'
    url = session.api_base_url + get_project_id_endpoint
    url = url.replace(':id', str(project_id))
    response = session.req.get(url)
    if response.status_code > 200:
        session.print_error_message(response)
    return response