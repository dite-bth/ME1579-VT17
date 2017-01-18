#!/bin/bash

# Run /w $sudo ./pip-venv.sh

# python3-pip and virtualenv should be installed
apt-get install python3-pip python3-venv
# if you need to create a virtual env in your shared folder (i.e /vagrant):
# $virtualenv --always-copy nameOfEnv
pip3 install virtualenv