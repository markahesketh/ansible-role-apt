# Ansible Role: Apt

[![Build Status](https://travis-ci.org/markahesketh/ansible-role-apt.svg?branch=master)](https://travis-ci.org/markahesketh/ansible-role-apt)

Ansible role to install and uninstall packages via Apt, a package manager for Debian-based systems.

## Installation

```
ansible-galaxy install markahesketh.apt
```

## Role Variables

Default values are listed below (see [`defaults/main.yml`](defaults/main.yml)):

```yml
apt_packages_install: []
apt_packages_uninstall: []
```

The `apt_packages_install` and `apt_packages_uninstall` variables take an array of package names. For example:

```yml
apt_packages_install:
  - vim
  - htop
  - tree

apt_packages_install:
  - cowsay
```

## Dependencies

None.

## Example Playbook

```yml
- hosts: web
  roles:
    - markahesketh.apt
```

## Testing

    molecule test

Requires [Molecule](https://molecule.readthedocs.io/en/latest/) and [Docker](https://docs.docker.com/engine/installation/).

## License

This role is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).

## Author

By [Mark Hesketh](https://www.markhesketh.co.uk/), a web developer from Manchester, UK.