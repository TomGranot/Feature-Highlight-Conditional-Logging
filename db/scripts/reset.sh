psql -h 127.0.0.1 -U postgres <<EOF
\x
REVOKE CONNECT ON DATABASE myapp FROM public;  DROP DATABASE myapp;  CREATE DATABASE myapp;  CREATE USER myapp WITH PASSWORD '5726127e9c457001c1075e14078662de';  ALTER ROLE myapp SET client_encoding TO 'utf8'; ALTER ROLE myapp SET default_transaction_isolation TO 'read committed';  ALTER ROLE myapp SET timezone TO 'UTC';  GRANT ALL PRIVILEGES ON DATABASE myapp TO myapp;
EOF