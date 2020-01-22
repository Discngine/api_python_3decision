# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 15:08:26 2020

@author: RaphaëlBerthier
"""

def __post_structure__(session, archive_path : str):
    session.check_token_expiration()
    try:
        with open(archive_path, 'rb') as archive:
            response = session.req.post(
                url         = session.base_url + session.post_structure_endpoint,
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
