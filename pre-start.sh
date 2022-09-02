#! /usr/bin/env bash

set -e

alembic upgrade head
uvicorn run:app --host 0.0.0.0
