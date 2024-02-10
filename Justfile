set dotenv-load := true

@_default:
    just --list

# ----------------------------------------------------------------------
# RELEASING
# ----------------------------------------------------------------------

bump:
    rye run bumpver update
    @just generate-examples && git add . && git commit -m "regenerate examples"

_generate-example DATA_FILE:
    #!/usr/bin/env bash
    DIRECTORY="{{ trim_end_match(DATA_FILE, '.yml') }}"
    rm -rf $DIRECTORY
    rye run copier copy -r HEAD . $DIRECTORY --force --data-file {{ DATA_FILE }}

@generate-examples:
    for file in `ls examples/*.yml`; do \
        just _generate-example $file; \
    done

# ----------------------------------------------------------------------
# UTILS
# ----------------------------------------------------------------------

# format justfile
fmt:
    just --fmt --unstable

# run pre-commit on all files
lint:
    pre-commit run --all-files
