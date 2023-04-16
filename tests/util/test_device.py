import pytest
import mock

from src.util.dev import Device


class TestDeviceClass():
    def test_same_device_id(self):
        obj1 = Device('a')
        obj2 = Device('a')

        assert obj1 == obj2

    def test_different_device_id(self):
        obj1 = Device('a')
        obj2 = Device('b')

        assert obj1 != obj2

    def test_different_device_id_and_same_device_name(self):
        obj1 = Device('a', 'name1')
        obj2 = Device('b', 'name1')

        assert obj1 != obj2

    def test_different_device_id_and_different_device_name(self):
        obj1 = Device('a', 'name1')
        obj2 = Device('b', 'name2')

        assert obj1 != obj2
