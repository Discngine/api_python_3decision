# 3decision_python_api
This is a small python wrapper for the 3decision REST API. Feel free to use it if you want. Else you can find a full documentation of the current official (3decision REST API here)[https://app.swaggerhub.com/apis/3decision/3decision/1.0.0#/]

# Set up

## Programmatic access to 3decision
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

Note, only for on-prem installations you need to provide your password. Specify an email address if you want to get notified with details on the progress of longer structure registration jobs (POST structure endpoint).

### How do I get the API Secret?
Connect to 3decision and go to your user preferences. Open API and generate a new key. You can set a custom expiration period.

![Click on User Preferences](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_1.png "Click on User Preferences")
![Open API](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_2.png "Open API")
![Fill out form](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_3.png "Fill out Form")
![Copy key](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_4.png "Copy key")



# Example usage

```python
from api_python_3decision import api

response=api.get_structure('1uyd')
api.post_structure('pathtoarchive.zip')
response=api.get_project_id('My New Project')
```

# Post Structure Endpoint
In order to register one or several structures you can use the post_structure function. You should specify a zip file containing all information required for such an upload. 
