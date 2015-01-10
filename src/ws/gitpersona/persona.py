import argparse
import re
import subprocess


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Specify or list repository-local persona(s).')
    parser.add_argument('--name', '-n', help='persona name')
    options = parser.parse_args(argv)
    personas = list_personas()
    if options.name:
        pass
    else:
        print('Known personas:')
        for name, persona in personas.items():
            print('  {persona} {name} <{email}>'.format(
                persona=name.ljust(12), **persona))
        print('Current username:')
        print('  {name} <{email}>'.format(
            name=cmd('git config user.name').strip(),
            email=cmd('git config user.email').strip()))


CONFIG_PERSONA = re.compile('^persona\\.(.*?) ([^<]*) <(.*?)>$')


def list_personas():
    result = {}
    config = cmd('git config --global --get-regex ^persona\\.')
    for line in config.splitlines():
        match = CONFIG_PERSONA.search(line)
        if not match:
            continue
        result[match.group(1)] = {
            'name': match.group(2), 'email': match.group(3)}
    return result


def cmd(cmd):
    process = subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout
