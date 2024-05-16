#!/bin/bash
set -e
if [ "$ENV" = 'DEV' ]; then
  echo "Server Development"
  exec python "aplikasi.py"
elif [ "$ENV" = 'UNIT' ]; then
  echo "Unit Tests"
  exec python "test.py"
else
  echo "Server Production"
  exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/aplikasi.py --callable app --stats 0.0.0.0:9191
fi