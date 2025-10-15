import os
import re
import subprocess

from semantic_version import Version
from specfile import Specfile

def get_prefix(specfile_name: str):
    return "mesa-" if specfile_name == "mesa" else "v"

def populate_repo_tags(repo: str, specfile_name: str):
    tags = subprocess.check_output(f"./grab_git_repo_tags.sh {repo}", shell=True, encoding="utf8").split()
    repo_tag_regex = re.compile(rf"^{get_prefix(specfile_name)}(\d+)\.(\d+)\.(\d+)$")
    tags = [tag for tag in tags if repo_tag_regex.match(tag) is not None]

    return tags

for i in os.scandir("specfiles/"):
    specfile = Specfile(i.path, autosave=True)
    specfile_ver = specfile.version
    specfile_url = specfile.url

    file_name = os.fsdecode(i.name).split(".")[0]
    repo_tags = populate_repo_tags(specfile_url, file_name)
    latest_version = repo_tags[-1].removeprefix(get_prefix(file_name))

    if Version(latest_version) < Version(specfile_ver) :
        print(f"no update available for {file_name}")
        print(f"current version is {specfile_ver}")
        continue

    print(f"new update available for {file_name}, version: {latest_version}")
    specfile.version = repo_tags[-1]
    os.system(f"./start_copr_build.sh {file_name}")
