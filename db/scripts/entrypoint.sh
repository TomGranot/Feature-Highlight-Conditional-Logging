#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE myapp;
    CREATE USER myapp WITH PASSWORD '5726127e9c457001c1075e14078662de';
    ALTER ROLE myapp SET client_encoding TO 'utf8';
    ALTER ROLE myapp SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myapp SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE myapp TO myapp;
EOSQL
