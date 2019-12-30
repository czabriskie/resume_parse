# tests loading the resume
import pytest
import os
from load_resume import load_resume

# check if function checks if file is a doc or pdf and raises an exception if
# it is not
#TODO
def test_check_file_type(tmpdir):
    d = tmpdir.mkdir("load_resume")
    tmp_resume = d.join('fake_resume.json')
    with pytest.raises("The document passed to the function was not a doc or pdf"):
        load_resume(tmp_resume)

def test_wrong_file_path()
