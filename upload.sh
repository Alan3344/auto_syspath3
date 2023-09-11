# test local install
# python setup.py install

pip install --upgrade pip
pip install --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
twine check dist/*
twine upload --repository pypi dist/* --verbose
# twine upload -r pypi dist/* --verbose

# [notice] A new release of pip is available: 23.2 -> 23.2.1
# [notice] To update, run: pip install --upgrade pip
# Checking dist/auto_syspath3-1.0-py3-none-any.whl: PASSED
# Checking dist/auto_syspath3-1.0.tar.gz: PASSED
# Uploading distributions to https://upload.pypi.org/legacy/
# Uploading auto_syspath3-1.0-py3-none-any.whl
# 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.6/12.6 kB • 00:00 • ?
# Uploading auto_syspath3-1.0.tar.gz
# 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.1/13.1 kB • 00:00 • ?

# View at:
# https://pypi.org/project/auto-syspath3/1.0/
