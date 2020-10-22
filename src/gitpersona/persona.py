import argparse
import re
import subprocess


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Specify or list repository-local persona(s).')
    parser.add_argument('--name', '-n', help='persona name')
    options = parser.parse_args(argv)
    personas = get_personas()
    if options.name:
        persona = personas.get(options.name)
        if not persona:
            print('Persona "{}" not found'.format(options.name))
            raise SystemExit(1)
        print('Setting user.name="{name}", user.email="{email}"'.format(
            **persona))
        set_persona(persona)
    else:
        print('Known personas:')
        for name, persona in personas.items():
            print('  {persona} {name} <{email}>'.format(
                persona=name.ljust(12), **persona))
        print('Current username:')
        print('  {name} <{email}>'.format(
            name=cmd('git config user.name'),
            email=cmd('git config user.email')))


def get_personas():
    results = {}
    entries = re.compile(r"^persona\W(?P<profile>[a-zA-Z0-9]+)\W(?P<param>[a-zA-Z0-9]+)\W(?P<value>.*)$", re.MULTILINE)

    config = cmd(f"git config --global --get-regex '^persona.([a-zA-Z0-9]+).*$'")
    for match in [e.groupdict() for e in entries.finditer(config)]:
        param = {match['param']: match['value']}
        if match['profile'] in results.keys():
            results.update({
                match['profile']: {**results[match['profile']], **param}
            })
        else:
            results.update({match['profile']: param})

    return results


def set_persona(persona):
    for p, v in persona.items():
        cmd(f'git config --local user.{p} "{v}"')


def cmd(cmd):
    process = subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, _ = process.communicate()
    # XXX This simply assumes utf8 -- is that feasible?
    return stdout.strip().decode('utf8')


if __name__ == '__main__':
    main()
