set dotenv-load := true

@_default:
    just --list

# ----------------------------------------------------------------------
# RELEASING
# ----------------------------------------------------------------------

_bump *ARGS:
    rye run bumpver update {{ ARGS }}

create-release:
    #!/usr/bin/env bash
    changes=$(git log $(git tag --sort=-creatordate | head -n 1)..HEAD --pretty=format:"- `%h`: %s")
    new_version=$(just _bump --dry 2>&1 | rg 'New Version' | awk '{print $5}')
    release_branch="release-v${new_version}"
    git checkout -b "${release_branch}"
    just _bump
    pr_title=$(git log -1 --pretty=%s)
    just generate-examples
    git add .
    git commit -m "regenerate examples for version ${new_version}"
    git push --set-upstream origin "${release_branch}"
    gh pr create --base main --head "${release_branch}" --title "${pr_title}" --body "${changes}"

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
