#!/bin/bash

echo "Installation process begin..."
python -m pip install --upgrade pip
pip install -r department-app/requirements.txt
python setup.py -q install
echo "Installation process finished"