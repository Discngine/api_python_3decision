# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:11:19 2020

@author: 3decision
"""

def __get_structure_metadata__(session, code : str):
    session.check_token_expiration()
    get_structure_endpoint = '/structure/:code/metadata'
    url = session.api_base_url + get_structure_endpoint
    url = url.replace(':code', code)
    response = session.req.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            print('Structure Not Found')
        else:
            print('Could not retreive structure')
    return response


def __get_structure_ligands__(session, code : str):
    session.check_token_expiration()
    get_structure__ligands_endpoint = '/structure/:code/ligands'
    url = session.api_base_url + get_structure__ligands_endpoint
    url = url.replace(':code', code)
    response = session.req.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            print('Structure Not Found')
        else:
            print('Could not retreive structure')
    return response     


def __post_structure__(session, archive_path : str):
    session.check_token_expiration()
    post_structure_endpoint = '/structure'
    try:
        with open(archive_path, 'rb') as archive:
            response = session.req.post(
                url         = session.api_base_url + post_structure_endpoint,
                files       = {'file' : ('post-structure.zip', archive, 'application/zip')},
                data        = {'mail' : session.mail}
            )
            if response.status_code != 202:
                print("Error in structure registration")
    except IOError:
        print("File not found")
    finally:
        archive.close()
    return response