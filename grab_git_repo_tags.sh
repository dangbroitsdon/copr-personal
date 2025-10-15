_git_repo_tags=$(git -c 'versionsort.suffix=-' \
            ls-remote --exit-code --refs --sort='version:refname' --tags "$1" '*.*' \
            | cut --delimiter='/' --fields=3)
echo "$_git_repo_tags"