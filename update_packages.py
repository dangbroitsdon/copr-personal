import os
import re
from compare_versions import is_new_version_available
from specfile import Specfile
from ghapi.all import GhApi

for i in os.scandir("specfiles/"):
    specfile = Specfile(i.path, autosave=True)
    specfile_url = specfile.url.removeprefix("https://github.com/")
    specfile_ver = specfile.version

    file_name = os.fsdecode(i.name).split(".")[0]

    gh_repo = GhApi(repo=file_name, owner=specfile_url.split("/")[0])
    gh_repo_tags = gh_repo.list_tags()

    gh_repo_tag_vers = []

    new_version_available = False

    for gh_repo_tag in gh_repo_tags:
        gh_repo_tag_ver = gh_repo_tag.ref.split("/")[2].removeprefix("v")
        gh_repo_tag_regex = re.compile(r".*-.*")

        if gh_repo_tag_regex.match(gh_repo_tag_ver) != None:
            continue

        gh_repo_tag_vers.append(gh_repo_tag_ver)

    for ver in gh_repo_tag_vers:
        if is_new_version_available(ver, specfile_ver):
            new_version_available = True
            specfile.version = ver
            break

    if new_version_available:
        print(f"new update available for {file_name}")
        os.system(f"./start_copr_build.sh {file_name}")
