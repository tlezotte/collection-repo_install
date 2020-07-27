# molecule/default/tests/test_default.py
import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_scl_repo_dir(host):
    sysinfo = host.system_info
    
    if sysinfo.distribution == "centos" and sysinfo.release == "7":
        rpm = host.package("centos-release-scl")
        assert rpm.is_installed
