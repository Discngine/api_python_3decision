# auth_type authorized values =   cloud  |  on_prem

# For 'on_prem' authentication, the following properties of the params object must be defined:
# base_url, user, mail, password, verifySSL must be defined

# For 'cloud' authentication, the following properties of the params object must be defined:
# base_url, user, mail, x_api_secret, verifySSL must be defined

# base_url example: https://3decision.discngine.cloud
# api_path_example: /api/v2

params = {
    'base_url'          : 'https://vm3decdv02.discngine.com:9003',
    'api_path'          : '/api/v2', 
    'internal_api_path' : '/internal/api', 
    'auth_type'         : 'on_prem',
    'x_api_secret'      : '',
    'mail'              : 'ppuser@foo.bar',
    'user'              : 'ppuser',
    'password'          : 'ppuser',
    'verifySSL'         : True
}


