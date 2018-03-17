from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

default_task = ["install_dependencies", "publish"]

BUILD_DEPENDENCIES = ["requests"]

@init
def init(project):
    for dependency in BUILD_DEPENDENCIES:
        project.build_depends_on(dependency)

    project.set_property('unittest_module_glob', 'test_*')
