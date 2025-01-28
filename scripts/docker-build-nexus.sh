#!/usr/bin/env bash

cd ../nexus || exit 1

docker build -t nexus .
