from enhanced_versioning import SemanticVersion

def is_new_version_available(ver1: str, ver2: str):
    semvar1 = SemanticVersion(ver1)
    semvar2 = SemanticVersion(ver2)

    if semvar1.major > semvar2.major:
        return True
    elif semvar1.minor > semvar2.minor:
        return True
    elif semvar1.patch > semvar2.patch and semvar1.minor == semvar2.minor:
        return True
    else:
        return False
