# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:53:17 2020

@author: 3decision
"""

def __get_project_ids__(session, project_name : str):
    session.check_token_expiration()
    get_project_id_endpoint = '/project/:name/ids'
    url = session.api_base_url + get_project_id_endpoint
    url = url.replace(':name', project_name)
    response = session.req.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            print('Project Not Found')
        else:
            print('Could not retreive project ids')
    return response