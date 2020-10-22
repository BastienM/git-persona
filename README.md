git-persona
===========

Fork of [wosc/git-persona](https://github.com/wosc/git-persona) (unmaintained since 2018).

git-persona provides an easy way to configure the git username on a per
repository basis. It is inspired by the mercurial extension
[hg-persona](https://bitbucket.org/0branch/hg-persona).

*git-persona* requires Python 3.3+ and can be installed from PyPI:

    $ pip install git-persona

Or manually:

    $ git clone https://github.com/bastienm/git-persona
    $ cd git-persona && python setup.py install.

You can configure invidual personas in your `~/.gitconfig` as follows:

    [persona "home]
        name = Firstname Lastname
        email = firstname@home.domain
        # other user.* setting
    [persona "work]  
        name = Firstname Lastname
        email = firstname.lastname@work.domain
        signingkey = 000AAA111BBB

and you'll probably want to set up an alias like this:

    [alias]
    persona = !git-persona

Then you can switch the persona of a repository:

    $ git persona -n home
    $ git persona -n work

And list all known personas:

    $ git persona
