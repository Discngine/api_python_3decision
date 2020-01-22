# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:11:19 2020

@author: RaphaëlBerthier
"""

def __get_structure__(session, code : str):
    session.check_token_expiration()
    url = session.api_base_url + session.get_structure_endpoint
    url = url.replace(':code', code)
    response = session.req.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            print('Structure Not Found')
        else:
            print('Could not retreive structure')
    return response
        
   

