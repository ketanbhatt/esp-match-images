#! /bin/bash

cd express_esp
npm start &

cd ../django_esp_project
pythonbrew venv use squadRun
python manage.py runserver &

cd ..