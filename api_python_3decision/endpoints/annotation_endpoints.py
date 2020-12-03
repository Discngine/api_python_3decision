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

