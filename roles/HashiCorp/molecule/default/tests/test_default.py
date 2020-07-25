# molecule/default/tests/test_default.py
import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("path", [
    ("/etc/yum.repos.d/hashicorp.repo"),
])
def test_hashicorp_repo_dir(host, path):
    r = host.file(path)

    assert r.exists
    assert r.user == "root"
    assert r.group == "root"
    assert r.mode == 0o644


def test_yum_utils_is_installed(host):
    rpm = host.package("yum-utils")
    assert rpm.is_installed
