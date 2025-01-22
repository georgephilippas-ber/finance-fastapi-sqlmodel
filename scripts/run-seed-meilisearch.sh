#!/usr/bin/env bash

cd ..
export PYTHONPATH=$(pwd)
python ./seeder/meilisearch/seed_meilisearch.py
