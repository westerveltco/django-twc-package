set dotenv-load := true

@_default:
    just --list

_generate-example DATA_FILE:
    rye run copier copy -r HEAD . {{ trim_end_match(DATA_FILE, '.yml') }} --force --data-file {{ DATA_FILE }}

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
