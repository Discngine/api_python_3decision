#author alex@discngine.com
#3decision API docker
#date 24/08/2020
#
#USAGE
#docker build -t discngine.azurecr.io/3decision/api .
#docker run -v 3dec_api:/3dec_api_runtime -it --rm --name 3dec_api_runtime discngine.azurecr.io/3decision/api

FROM python:3

WORKDIR /usr/src/app

#install gnutls-bin to get 3decision certificate
RUN apt-get update && apt-get install -y \
    vim \
    gnutls-bin \
 && rm -rf /var/lib/apt/lists/*

#clone 3decision api
RUN git clone https://github.com/Discngine/api_python_3decision

WORKDIR /usr/src/app/api_python_3decision
#install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#set symlinks to start/configuration files
RUN mkdir /3dec_api_runtime
RUN touch /3dec_api_runtime/settings.py
RUN touch /3dec_api_runtime/3decision_commands.py
#RUN rm settings.py
RUN ln -s /3dec_api_runtime/settings.py settings.py

WORKDIR /usr/src/app
#install certificate
RUN gnutls-cli --print-cert 3decision.discngine.cloud:443 </dev/null| sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > 3decision.discngine.cloud.crt
ENV REQUESTS_CA_BUNDLE=/usr/src/app/3decision.discngine.cloud.crt

#link python script to working folder
RUN ln -s /3dec_api_runtime/3decision_commands.py 3decision_commands.py
#set python path for library import
ENV PYTHONPATH "${PYTHONPATH}:`pwd`"
CMD [ "python", "./3decision_commands.py" ]
