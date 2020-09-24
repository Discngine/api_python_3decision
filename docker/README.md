# Python 3decision REST API Wrapper in Docker
This is the Dockerfile for 3decision python api.

# Configure

```bash
mkdir api_conf
```
Inside the api_conf folder, put:
- settings.py
- 3decision_commands.py
You can also put these files in a docker volume.
3decision_commands.py must contain you python routine.


# Build
```bash
docker build -t 3decision_api .
```

# Run
```bash
docker run -v ./api_conf:/3dec_api_runtime \
      -it --rm --name 3dec_api_runtime discngine.azurecr.io/3decision/api
```
# Custom runtime
you can customize runtime with --entrypoint='xxx'

