# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:23:39 2020

@author: RaphaëlBerthier
"""

import requests
from datetime import datetime, timedelta
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_session(settings):
    session = Session(settings)
    if session.auth_type == 'on_prem':
        session.on_prem_authentication()    
    else:        
        session.cloud_authentication()
    return session

   
class Session():
    
    api_base_url   = str
    x_api_secret   = str
    mail           = str
    auth_type      = str
    user           = str
    password       = str
    token          = str
    verifySSL      = bool
    sec_exp_check  = 10
    expires        = datetime
    req            = requests.Session()
    
    token_endpoint = '/token'
    login_endpoint = '/login'
    post_structure_endpoint = '/structure'
    get_structure_endpoint = '/structure/:code/metadata'
    get_project_id_endpoint = '/project/:name/ids'
    
    def __init__(self, settings):
        self.api_base_url   = settings['base_url'] + settings['api_path']
        self.auth_type      = settings['auth_type']
        self.mail           = settings['mail']
        if self.auth_type == 'on_prem':
            self.user           = settings['user']
            self.password       = settings['password']
            self.verifySSL      = settings['verifySSL']
        else:
            self.x_api_secret   = settings['x_api_secret']
        
    def on_prem_authentication(self):
        response = self.req.post(
                url = self.api_base_url + self.login_endpoint,
                verify=self.verifySSL,
                data = {'username':self.user},
                auth = requests.auth.HTTPBasicAuth(self.user, self.password)
        )
        if response.status_code == 200:
            print("Logged in")
        else:
            print("Error login in")
        
               
    def cloud_authentication(self):
        print('Generating token ...')
        response = self.req.get(
            url = self.api_base_url + self.token_endpoint, 
            headers = {'x-api-secret' : self.x_api_secret}
        )
        response_json = response.json()
        status_code = response.status_code
        if (status_code == 200):
            data = response_json['data']
            self.token = data['token']
            curr_date = datetime.now()
            expiration_time = timedelta(seconds=data['expires'])
            self.expires = curr_date + expiration_time
            self.req.headers['Authorization'] = 'Bearer ' + self.token
            print('New token generated.')
        else:
            raise Exception('Could not get token')
    
    def check_token_expiration(self):
        if self.auth_type == 'cloud':
            if self.token != '':
                expires_delta = self.expires - datetime.now()
                if expires_delta.seconds < self.sec_exp_check:
                    print('Token has expired...')
                    self.cloud_authentication()
            else:
                self.cloud_authentication()
