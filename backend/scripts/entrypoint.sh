#!/usr/bin/env bash
set -euo pipefail;

COMMAND="$@"

function poll_postgres {
python <<-END
import sys
import psycopg2
import environ

try:
    env = environ.Env()
    
    dbname = env.str('POSTGRES_DB')
    user = env.str('POSTGRES_USER')
    password = env.str('POSTGRES_PASSWORD')
    host = env.str('POSTGRES_HOST')

    conn = psycopg2.connect(
      dbname=dbname,
      user=user,
      password=password,
      host=host,
      port=5432
    )
except psycopg2.OperationalError:
    sys.exit(-1)

sys.exit(0)
END
}

until poll_postgres; do
  >&2 echo "postgres is not ready yet, sleeping..."
  sleep 1
done

>&2 echo "postgres is ready, continue the journey..."
exec $COMMAND
