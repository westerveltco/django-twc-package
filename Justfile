set dotenv-load := true

@_default:
    just --list

# ----------------------------------------------------------------------
# RELEASING
# ----------------------------------------------------------------------

_bump *ARGS:
    rye run bumpver update {{ ARGS }}

create-release:
    new_version=$(just _bump --dry | rg 'New Version' | awk '{print $4}')
    git checkout -b "release-v${new_version}"
    just _bump
    pr_title=$(git log -1 --pretty=%s)
    @just generate-examples
    git add .
    git commit -m "regenerate examples"
    git push --set-upstream origin "release-v${new_version}"
    gh pr create --base main --head "release-v${new_version}" --title "${pr_title}"--body "This PR includes the changes for the new release v${new_version}."

_generate-example DATA_FILE:
    #!/usr/bin/env bash
    DIRECTORY="{{ trim_end_match(DATA_FILE, '.yml') }}"
    rm -rf $DIRECTORY
    rye run copier copy -r HEAD . $DIRECTORY --force --trust --data-file {{ DATA_FILE }}

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
