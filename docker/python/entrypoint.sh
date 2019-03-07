#!/usr/bin/env bash
gunicorn --reload djangoapiintegration.wsgi -c ./gunicorn.py -b 0.0.0.0:8888
