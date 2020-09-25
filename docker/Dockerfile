#author alex@discngine.com
#3decision API docker
#date 24/08/2020
#
#USAGE
#docker build -t discngine.azurecr.io/3decision/api .
#docker run -v 3dec_api:/3dec_api_runtime -it --rm --name 3dec_api_runtime discngine.azurecr.io/3decision/api

FROM python:3

# setup args for installation
ARG MAXITVER=11.100
ARG MAXITNAME=maxit-v$MAXITVER-prod-src
ARG MAXITTARGZ=$MAXITNAME.tar.gz
ARG MAXITSOURCE=https://sw-tools.rcsb.org/apps/MAXIT/$MAXITTARGZ

# update repository information
RUN apt-get update --fix-missing

# install curl utils so we can download source
RUN apt-get install -y --no-install-recommends \
 gnupg2 curl ca-certificates

# install some packages for development (optional)
RUN apt-get install -y --no-install-recommends \
     vim git

# install utils to build source
RUN apt-get install -y --no-install-recommends \
   build-essential

# additional (undeclared in documentation) dependencies
RUN apt-get install -y --no-install-recommends \
   bison flex tcsh

# maxit install time!
RUN mkdir -p /usr/local/maxit
# download source, expand, build
RUN cd /usr/local/maxit && \
    curl -fsSL -O $MAXITSOURCE && \
    tar -zxf $MAXITTARGZ && \
    cd $MAXITNAME && \
    make binary

# setup env vars for install/runtime
ENV RCSBROOT=/usr/local/maxit/$MAXITNAME
ENV PATH="$RCSBROOT/bin":$PATH
RUN chmod 775 /usr/local/maxit/$MAXITNAME -R

# cleanup
RUN rm -f /usr/local/maxit/$MAXITTARGZ
RUN apt-get purge --auto-remove -y \
    gnupg2 curl ca-certificates \
    build-essential bison flex tcsh


WORKDIR /usr/src/app

#install gnutls-bin to get 3decision certificate
RUN apt-get update && apt-get install -y \
    gnutls-bin

# cleanup install cache
RUN rm -rf /var/lib/apt/lists/*

#clone 3decision api
ENV GIT_SSL_NO_VERIFY=1
RUN git clone https://github.com/Discngine/api_python_3decision

WORKDIR /usr/src/app/api_python_3decision
#install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Customer requirement (this should be removed from here)
RUN pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org sqlalchemy pymysql

#set symlinks to start/configuration files
RUN mkdir /3dec_api_input
RUN mkdir /3dec_api_recepies
RUN mkdir /3dec_api_config
RUN touch /3dec_api_config/settings.py
RUN touch /3dec_api_config/3decision_commands.py
RUN rm settings.py
RUN ln -s /3dec_api_config/settings.py settings.py

WORKDIR /usr/src/app
#install certificate
RUN gnutls-cli --print-cert 3decision.discngine.cloud:443 </dev/null| sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > 3decision.discngine.cloud.crt
ENV REQUESTS_CA_BUNDLE=/usr/src/app/3decision.discngine.cloud.crt

#link python script to working folder
RUN ln -s /3dec_api_config/3decision_commands.py 3decision_commands.py
#set python path for library import
ENV PYTHONPATH "${PYTHONPATH}:`pwd`"
CMD [ "python", "./3decision_commands.py" ]
