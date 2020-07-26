# molecule/default/tests/test_default.py
import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_epel_repo_dir(host):
    f = host.file("/etc/yum.repos.d/epel.repo")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_powertools_repo_dir(host):
    sysinfo = host.system_info
    
    if sysinfo.distribution == "centos" and sysinfo.release == "8":
        f = host.file("/etc/yum.repos.d/CentOS-PowerTools.repo")

        assert f.exists
        assert f.user == "root"
        assert f.group == "root"
        assert f.mode == 0o644
        #assert f.contains("enabled=1")
        #assert host.run('yum repoinfo PowerTools|grep enabled').rc == 0
