# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:44:08 2020

@author: 3decision
"""

def __ligand_search__(session, search_type: str, input_type : str, input_value : str):
    session.check_token_expiration()
    search_ligand_endpoint = '/ligand/search/:searchType/:inputType/:input'
    url = session.api_base_url + search_ligand_endpoint
    url = url.replace(':searchType', search_type)
    url = url.replace(':inputType', input_type)
    url = url.replace(':input', input_value)
    response = session.req.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            print('Ligand Not Found')
        else:
            print('Could not retreive ligands')
    return response
        
