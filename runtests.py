#!/usr/bin/env python
import sys
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

import django
from django.conf import settings
from django.test.utils import get_runner


def runtests():
    if hasattr(django, 'setup'):
        django.setup()
    apps = sys.argv[1:] or ['appodeal', ]
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(apps)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
