# -*- coding: utf-8 -*-
"""
Created on Tue Dec 3 2020

@author: Peter Schmidtke
"""

def _post_biomolecule_annotation(session, data : str):
    session.check_token_expiration()
    endpoint_path = '/biomolecule/annotation'
    response = session.req.post(
        url         = session.api_base_url + endpoint_path,
        json        = data
    )

    if response.status_code > 202:
        session.print_error_message(response)

    return response


def _post_biomolecule_annotation_input_type(session, data : str,input_type:str, input_str:str):
    session.check_token_expiration()
    endpoint_path = '/biomolecule/annotation/'+input_type+'/'+input_str
    response = session.req.post(
        url         = session.api_base_url + endpoint_path,
        json        = data
    )

    if response.status_code > 202:
        session.print_error_message(response)

    return response

