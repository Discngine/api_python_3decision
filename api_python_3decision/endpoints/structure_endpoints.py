# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:11:19 2020

@author: 3decision
"""


def _get_structure(session, code : str):
    session.check_token_expiration()
    endpoint_path = '/structure/:code'
    url = session.api_base_url + endpoint_path
    url = url.replace(':code', code)
    response = session.req.get(url)
    if response.status_code > 202:
        session.print_error_message(response)
    return response


def _get_structure_metadata(session, code : str):
    session.check_token_expiration()
    endpoint_path = '/structure/:code/metadata'
    url = session.api_base_url + endpoint_path
    url = url.replace(':code', code)
    response = session.req.get(url)
    if response.status_code > 202:
        session.print_error_message(response)
    return response


def _get_structure_ligands(session, code : str):
    session.check_token_expiration()
    endpoint_path = '/structure/:code/ligands'
    url = session.api_base_url + endpoint_path
    url = url.replace(':code', code)
    response = session.req.get(url)
    if response.status_code > 202:
        session.print_error_message(response)
    return response     

def _put_reanalyze_structure(session, code : str):
    session.check_token_expiration()
    endpoint_path = '/structure/:code/reanalyze'
    url = session.api_base_url + endpoint_path
    url = url.replace(':code', code)
    response = session.req.put(url)
    if response.status_code > 202:
        session.print_error_message(response)
    return response 

def _post_structure(session, archive_path : str):
    session.check_token_expiration()
    endpoint_path = '/structure'
    try:
        with open(archive_path, 'rb') as archive:
            response = session.req.post(
                url         = session.api_base_url + endpoint_path,
                files       = {'file' : ('post-structure.zip', archive, 'application/zip')},
                data        = {'mail' : session.mail}
            )
            if response.status_code > 202:
                session.print_error_message(response)
    except IOError:
        print("File not found")
    finally:
        archive.close()
    return response
    

def _delete_structure(session, code : str):
    session.check_token_expiration()
    endpoint_path = '/structure/:code'
    url = session.api_base_url + endpoint_path
    url = url.replace(':code', code)
    response = session.req.delete(url)
    if response.status_code > 202:
        session.print_error_message(response)
    return response 
    
def _search_structure_by_anotation(session, annotation_type:  str, annotation_value: str):
    session.check_token_expiration()
    endpoint_path = '/structure/search/annotation/:annotationType/:annotation/metadata'
    url = session.api_base_url + endpoint_path
    url = url.replace(':annotationType', annotation_type)
    url = url.replace(':annotation', annotation_value)
    response = session.req.get(url)
    if response.status_code > 202:
        session.print_error_message(response)
    return response 
    
    
    