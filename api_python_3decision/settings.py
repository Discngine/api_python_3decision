# auth_type authorized values =   cloud  |  on_prem

# For 'on_prem' authentication, the following properties of the params object must be defined:
# base_url, user, mail, password, verifySSL must be defined

# For 'cloud' authentication, the following properties of the params object must be defined:
# base_url, user, mail, x_api_secret, verifySSL must be defined

# base_url example: https://3decision.discngine.cloud
# api_path_example: /api/v2

params = {
    'base_url'          : '',
    'api_path'          : '/api/v2', 
    'auth_type'         : '',
    'x_api_secret'      : '',
    'mail'              : '',
    'user'              : '',
    'password'          :  '',
    'verifySSL'         : True,
    'proxy'             : {'http': '', 'https':''}
}


