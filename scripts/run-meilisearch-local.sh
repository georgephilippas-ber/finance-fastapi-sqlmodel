#!/usr/bin/env bash

OS=$(uname)

MASTER_KEY="jYRlnO2U1liwOSdm9CjTPFS1HZuBjeaLK3gh2NXcr28"

if [[ "$OS" == "Linux" ]]; then
    :
elif [[ "$OS" == "Darwin" ]]; then
    :
elif [[ "$OS" == CYGWIN* || "$OS" == MINGW* || "$OS" == MSYS* ]]; then
    meilisearch-windows-amd64 --master-key $MASTER_KEY
else
    echo "$OS"
fi
