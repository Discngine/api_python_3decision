# Python 3decision REST API Wrapper
This is a small python wrapper for the 3decision REST API. Feel free to use it if you want. Else you can find a full documentation of the current official [3decision REST API here](https://app.swaggerhub.com/apis-docs/3decision/3decision/1.0.0)

# Set up
Clone this repository to your computer. Make sure the path to this folder is available in your python path so you can load the module, and install the packages specified in the requirements.txt file

## Programmatic access to 3decision
Depending on how you access 3decision, using the public cloud or an on-premises installation you have to get your access token from 3decision and 
adapt the `settings.py` with your data.

### Example settings
Here an example to access the 3decision public cloud server:
```
    params = {
        'base_url'      : 'https://3decision.discngine.cloud',
        'api_path'      : '/api/v2',
        'auth_type'     : 'cloud',
        'x_api_secret'  : 'myFancySecretKeyIgotFrom3decisionForCloudAuthentication',
        'mail'          : 'my_mail@mail.com',
        'user'          : 'myUsername',
        'password'      : 'passwordForOnPremInstallationsOnly',
        'verifySSL'     : True
    }
```

Note, only for on-prem installations you need to provide your password. Specify an email address if you want to get notified with details on the progress of longer structure registration jobs (POST structure endpoint).
For cloud authentication, you will need to generate an API Secret Key.

### How do I get the API Secret?
Connect to 3decision and go to your user preferences. Open API and generate a new key. You can set a custom expiration period.

![Click on User Preferences](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_1.png "Click on User Preferences")
![Open API](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_2.png "Open API")
![Fill out form](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_3.png "Fill out Form")
![Copy key](https://github.com/Discngine/api_python_3decision/blob/master/images/3dec_screen_4.png "Copy key")

More [documentation](https://discngine.github.io/3decision-api-doc/v2/3decision%20API%20Secret%20Key%20and%20TokenDocumentation.pdf) on the secret key and token management is available 

# Example usage

```python
from api_python_3decision import api

# Structure endpoints:

response = api.get_structure('1uyd')
response = api.get_structure_metadata('1uyd')
response = api.get_structure_ligands('1uyd')
response = api.reanalyze_structure('1uyd')
response = api.post_structure('pathtoarchive.zip')
response = api.delete_structure('structureCodeIWantToDelete')

# Project endpoints:

response = api.get_project_ids('My New Project')
project_id = 1
response = api.get_project(project_id)

# Ligand endpoints
response = api.get_ligand_search('exact', 'smiles', 'CCCCn1c(Cc2cc(OC)c(OC)c(OC)c2Cl)nc2c(N)ncnc12')


```

# Endpoints
## Post Structure Endpoint
In order to register one or several structures you can use the post_structure function. You should specify a zip file containing all information required for such an upload. More information on how the specifications of that zip file can be found in the [POST Structure endpoint documentation](https://discngine.github.io/3decision-api-doc/v2/POST%20Structure%20Documentation.pdf). 
You can also download a [sample zip file](https://github.com/Discngine/api_python_3decision/blob/master/examples/post_structure.zip) to get you started.

When using the example archive, you will need to unzip it, change the user specified in the CREATED BY field by your own username, and rebuild the archive. Make sure to have the configuration file at the root of the archive :

![Copy key](https://github.com/Discngine/api_python_3decision/blob/master/images/archive.jpg "Archive schema example")
