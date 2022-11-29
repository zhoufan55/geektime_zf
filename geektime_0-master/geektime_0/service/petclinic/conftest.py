import json

import pytest
import requests

from geektime_0.service.petclinic.utils.log import log


def pytest_collection_modifyitems(config, items):
    """
    测试用例收集
    """
    log.debug("all items")
    log.debug(items)
    testcase_list = []

    cache = set()
    for item in items:
        testcase = {'name': item.nodeid, 'data': None}
        testcase_list.append(testcase)

        items = item.nodeid.split('::')
        for i in range(1, len(items)):
            suite_name = "::".join(items[0:i])
            if suite_name not in cache:
                suite = {'name': suite_name, 'data': None}
                testcase_list.append(suite)
                cache.add(suite_name)

        log.debug(testcase)
    with open('testcases.json', 'w') as f:
        json.dump(testcase_list, f, indent=2, ensure_ascii=False)


def pytest_collect_file(parent, file_path):
    if file_path.suffix == ".yaml" and file_path.name.startswith("test"):
        return YamlFile.from_parent(parent, path=file_path)


class YamlFile(pytest.File):
    def collect(self):
        # We need a yaml parser, e.g. PyYAML.
        import yaml

        raw = yaml.safe_load(self.path.open())
        for name, spec in sorted(raw.items()):
            name: str
            if name.startswith('test_'):
                yield YamlItem.from_parent(self, name=name, spec=spec)


class YamlItem(pytest.Item):
    def __init__(self, *, spec, **kwargs):
        super().__init__(**kwargs)
        self.spec = spec

    def runtest(self):
        for step in self.spec:
            # Some custom test execution (dumb example follows).
            step: dict
            for key, value in step.items():
                if key == 'get':
                    log.debug('request')
                    r = requests.get(**value)
                    log.debug(r.json())
                if key == 'find':
                    # driver.find()
                    log.debug("web")

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            return "\n".join(
                [
                    "usecase execution failed",
                    "   spec failed: {1!r}: {2!r}".format(*excinfo.value.args),
                    "   no further details known at this point.",
                ]
            )

    def reportinfo(self):
        return self.path, 0, f"usecase: {self.name}"


class YamlException(Exception):
    """Custom exception for error reporting."""
