#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CDUCourseSupportSystem.settings")

    from django.core.management import execute_from_command_line
#sorry this is jsut xample. delete it later.
    execute_from_command_line(sys.argv)
