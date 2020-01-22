# 3decision_python_api
This is a small python wrapper for the 3decision REST API. Feel free to use it if you want. Else you can find a full documentation of the current official (3decision REST API here)[https://app.swaggerhub.com/apis/3decision/3decision/1.0.0#/]

# Set up

## Access to 3decision
Depending on how you access 3decision, using the public cloud or an on-premises installation you have to get your access token from 3decision and 
adapt the `settings.py` with your data.

### Example settings
Here an example to access the 3decision public cloud server:
```
    params = {
        'base_url'      : 'https://3decision.discngine.cloud',
        'auth_type'     : 'cloud',
        'x_api_secret'  : 'myFancySecretKeyIgotFrom3decision',
        'mail'          : 'my_mail@mail.com',
        'user'          : 'myUsername',
        'password'      : 'passwordForOnPremInstallationsOnly',
        'verifySSL'     : True
    }
```



# Example usage

```python
from 3decision_python_api import api_3decision as api

response=api.get_structure('1uyd')
api.post_structure('pathtoarchive.zip')
response=api.get_project_id('My New Project')
```

# Post Structure Endpoint
In order to re
