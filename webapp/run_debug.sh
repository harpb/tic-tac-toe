#!/bin/bash

python server.py &
python manage.py runserver --noreload 8010 &

trap "kill -TERM -$$" SIGINT
wait