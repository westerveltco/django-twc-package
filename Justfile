set dotenv-load := true
set unstable := true

[private]
default:
    @just --list

[private]
fmt:
    @just --fmt

[private]
@generate-example DATA_FILE:
    #!/usr/bin/env bash

    set -euo pipefail

    DIRECTORY="{{ trim_end_match(DATA_FILE, '.yml') }}"
    rm -rf $DIRECTORY

    COMMAND="copier copy -r HEAD . $DIRECTORY --force --trust --data-file {{ DATA_FILE }}"
    if [ -z "$(command -v rye)" ]; then
        eval $COMMAND
    else
        rye run $COMMAND
    fi

bootstrap:
    uv python install
    uv sync --frozen

generate-examples:
    for file in `ls examples/*.yml`; do \
        just generate-example $file; \
    done

lint:
    uv run --with pre-commit-uv pre-commit run --all-files

lock *ARGS:
    uv lock {{ ARGS }}
