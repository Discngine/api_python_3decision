# 3decision_python_api
This is a small python wrapper for the 3decision REST API. Feel free to use it if you want. Else you can find a full documentation of the current official 3decision REST API here.

# Example usage

```python
from 3decision_python_api import api_3decision as api

api.get_structure('1uyd')
api.post_structure('pathtoarchive.zip')
api.get_project_id('My New Project')
```
