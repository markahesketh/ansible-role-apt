import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cowsay_is_installed(host):
    cowsay = host.package("cowsay")
    assert cowsay.is_installed


def test_vim_is_uninstalled(host):
    assert host.ansible("apt", "name=vim state=present")["changed"]
