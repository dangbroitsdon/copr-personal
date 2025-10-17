import os
import re
import subprocess

from semantic_version import Version
from specfile import Specfile

for i in os.scandir("specfiles/"):
    specfile = Specfile(i.path, autosave=True)
    specfile_filename = os.fsdecode(i.name).split(".")[0]
    specfile_url = specfile.url
    specfile_ver = specfile.version
    specfile_ver_prefix = "mesa-" if specfile_filename == "mesa" else "v"

    repo_tags = subprocess.check_output(f"./grab_git_repo_tags.sh {specfile_url}", shell=True, encoding="utf8").split()
    repo_tags = [repo_tag for repo_tag in repo_tags if re.compile(rf"^{specfile_ver_prefix}(\d+)\.(\d+)\.(\d+)$").match(repo_tag) is not None]

    latest_version = repo_tags[-1].removeprefix(specfile_ver_prefix)

    if Version(latest_version) > Version(specfile_ver):
        print(f"new update available for {specfile_filename}, latest version: {latest_version}, current version: {specfile_ver}")
        specfile.version = latest_version
        subprocess.run(f"./start_copr_build.sh {specfile_filename}")
        continue

    print(f"no update available for {specfile_filename}")
