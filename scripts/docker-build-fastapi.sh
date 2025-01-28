#!/usr/bin/env bash

cd .. || exit 1

docker build -t fastapi .
