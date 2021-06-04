#!/bin/bash

echo "Install process begin..."
python -m pip install --upgrade pip
pip install -r requirements.txt
python setup.py -q install