# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:23:39 2020

@author: 3decision
"""

import requests
from datetime import datetime, timedelta
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_session(settings):
    session = Session(settings)
    if session.auth_type == 'on_prem':
        print('Connecting to 3decision... (On Prem)')
        session.on_prem_authentication()    
    else:
        print('Connecting to 3decision... (Cloud)')
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
    #expires        = datetime
    #req            = requests.Session()
    
    token_endpoint = '/token'
    login_endpoint = '/login'
    
    def __init__(self, settings):
        self.expires = datetime
        self.req = requests.Session()
        self.api_base_url           = settings['base_url'] + settings['api_path']
        self.api_base_internal_url  = settings['base_url'] + settings['internal_api_path']
        self.auth_type              = settings['auth_type']
        self.mail                   = settings['mail']
        self.verifySSL              = settings['verifySSL']
        if self.auth_type == 'on_prem':
            self.user               = settings['user']
            self.password           = settings['password']
        else:
            self.x_api_secret       = settings['x_api_secret']
        
    def on_prem_authentication(self):
        response = self.req.post(
                url = self.api_base_url + self.login_endpoint,
                verify = self.verifySSL,
                data = {'username':self.user},
                auth = requests.auth.HTTPBasicAuth(self.user, self.password)
        )
        if response.status_code == 200:
            print("Logged in")
        else:
            print(response.text)
            print("Error login in")
        
               
    def cloud_authentication(self):
        print('Generating token ...')
        response = self.req.get(
            url = self.api_base_url + self.token_endpoint, 
            verify = self.verifySSL,
            headers = {'x-api-secret' : self.x_api_secret}
        )
        status_code = response.status_code     
        if (status_code == 200):
            response_json = response.json()
            data = response_json['data']
            self.token = data['token']
            curr_date = datetime.now()
            expiration_time = timedelta(seconds=data['expires'])
            self.expires = curr_date + expiration_time
            self.req.headers['Authorization'] = 'Bearer ' + self.token
            print('New token generated.')
        else:
            print('Failed authentication.\nResponse status code: ' + str(status_code) + '\n')
            raise Exception('Could not generate token')
    
    def check_token_expiration(self):
        if self.auth_type == 'cloud':
            if self.token != '':
                expires_delta = self.expires - datetime.now()
                if expires_delta.seconds < self.sec_exp_check:
                    print('Token has expired...')
                    self.cloud_authentication()
            else:
                self.cloud_authentication()
                
    def print_error_message(self, response):
        error = response.json()['error']
        print('\nError message:\t\t' + error['message'] + '\n' + 'Status Code:\t\t' + str(error['code']) + '\n' + 'Type:\t\t\t' + error['type'] + '\n')
        if 'details' in error:
            for detailled_error in error['details']:
                print('\nDetailed Error: \t' + detailled_error['message'] + '\n' + 'Status Code:\t\t' + str(detailled_error['code']) + '\n')