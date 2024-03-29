#!/bin/bash
set -euo pipefail

export PYTHONPATH="$(realpath $(dirname $0))"

if [ -z "${MUX_TOKEN_ID:-}" ]
then
      echo "MUX_TOKEN_ID not set"
      exit 255
fi

if [ -z "${MUX_TOKEN_SECRET:-}" ]
then
      echo "MUX_TOKEN_SECRET not set"
      exit 255
fi

VIDEO_TESTS=./examples/video/exercise*.py
for f in $VIDEO_TESTS
do
  echo "========== Running $f =========="
    python $f
done

DATA_TESTS=./examples/data/exercise*.py
for f in $DATA_TESTS
do
  echo "========== Running $f =========="
    python $f
done
