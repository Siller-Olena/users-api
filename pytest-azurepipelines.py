import sys

def test_python_version():
    python_version = sys.version_info
    print(f"Python Hauptversion: {python_version.major}")
    print(f"Python Nebenversion: {python_version.minor}")
    print(f"Python Patch-Level: {python_version.micro}")
    print(f"Python Release-Level: {python_version.releaselevel}")
    print(f"Python Serial: {python_version.serial}")
    print(f"Vollständige Python Version: {sys.version}")

    # Beispielhafte Assertions basierend auf der erwarteten Version
    assert python_version.major >= 3
    assert python_version.minor >= 8