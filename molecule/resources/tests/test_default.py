import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

@pytest.mark.parametrize("name", [
    "rh-php72",
    "rh-php72-php-devel",
    "rh-php72-php-fpm",
    "rh-php72-php-gd",
    "rh-php72-php-ldap",
    "rh-php72-php-mbstring",
    "rh-php72-php-opcache",
    "rh-php72-php-pdo",
    "rh-php72-php-pecl-apcu",
    "rh-php72-php-xmlrpc",
])
def test_php_packages_installed(host, name):
    pkg = host.package(name)
    assert pkg.is_installed
