#!/usr/bin/env bash

PORT=7700
MASTER_KEY="jYRlnO2U1liwOSdm9CjTPFS1HZuBjeaLK3gh2NXcr28"

OS=$(uname)
if [[ "$OS" == "Linux" ]]; then
    meilisearch --master-key=$MASTER_KEY
elif [[ "$OS" == "Darwin" ]]; then
    :
elif [[ "$OS" == CYGWIN* || "$OS" == MINGW* || "$OS" == MSYS* ]]; then
    meilisearch-windows-amd64 --master-key $MASTER_KEY --http-addr "0.0.0.0:${PORT}"
else
    echo "$OS"
fi
