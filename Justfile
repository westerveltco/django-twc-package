set dotenv-load := true

@_default:
    just --list

bootstrap *ARGS:
    rye sync {{ ARGS }}

lock *ARGS:
    rye lock {{ ARGS }}

# ----------------------------------------------------------------------
# EXAMPLES
# ----------------------------------------------------------------------

# generate all examples from examples/*.yml copier answer files
@generate-examples:
    for file in `ls examples/*.yml`; do \
        just _generate-example $file; \
    done

_generate-example DATA_FILE:
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

# ----------------------------------------------------------------------
# UTILS
# ----------------------------------------------------------------------

# format justfile
fmt:
    just --fmt --unstable

# run pre-commit on all files
lint:
    rye run pre-commit run --all-files
