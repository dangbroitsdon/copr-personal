import os
import re
import subprocess

from semantic_version import Version
from specfile import Specfile

def get_prefix(specfile_name: str):
    return "mesa-" if specfile_name == "mesa" else "v"

for i in os.scandir("specfiles/"):
    specfile = Specfile(i.path, autosave=True)
    specfile_ver = specfile.version
    specfile_url = specfile.url
    specfile_filename = os.fsdecode(i.name).split(".")[0]

    repo_tags = subprocess.check_output(f"./grab_git_repo_tags.sh {specfile_url}", shell=True, encoding="utf8").split()
    repo_tag_regex = re.compile(rf"^{get_prefix(specfile_filename)}(\d+)\.(\d+)\.(\d+)$")
    repo_tags = [repo_tag for repo_tag in repo_tags if repo_tag_regex.match(repo_tag) is not None]

    latest_version = repo_tags[-1].removeprefix(get_prefix(specfile_filename))

    if Version(latest_version) < Version(specfile_ver) :
        print(f"no update available for {specfile_filename}")
        continue

    print(f"new update available for {specfile_filename}, version: {latest_version}")
    specfile.version = repo_tags[-1]
    os.system(f"./start_copr_build.sh {specfile_filename}")