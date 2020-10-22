import os
import pytest
from persona import cmd, get_personas, set_persona


@pytest.fixture(scope='session')
def personas(request):
    testhome = {
        'name': 'First Last',
        'email': 'home@example.com'
    }
    for p, v in testhome.items():
        cmd(f'git config --global persona.testhome.{p} "{v}"')

    testwork = {
        'name': 'First Last',
        'email': 'work@example.com',
        'signingkey': '000AAA111BBB'
    }
    for p, v in testwork.items():
        cmd(f'git config --global persona.testwork.{p} "{v}"')

    def teardown():
        cmd('git config --global --unset persona.testhome')
        cmd('git config --global --unset persona.testwork')
    request.addfinalizer(teardown)


@pytest.fixture
def repository(request, tmpdir):
    cwd = os.getcwd()
    request.addfinalizer(lambda: os.chdir(cwd))
    os.chdir(str(tmpdir))
    cmd('git init')


def test_get_personas(personas):
    personas = get_personas()
    assert personas['testhome'] == {
        'name': 'First Last',
        'email': 'home@example.com'
    }
    assert personas['testwork'] == {    
        'name': 'First Last',
        'email': 'work@example.com',
        'signingkey': '000AAA111BBB'
    }


def test_set_persona(repository):
    set_persona(
        {'name': 'First Last', 'email': 'home@example.com'})
    assert 'First Last' == cmd('git config user.name')
    assert 'home@example.com' == cmd('git config user.email')
