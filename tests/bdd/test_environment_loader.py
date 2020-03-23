# coding=utf-8
"""Environment Loader feature tests."""

# from pypi
from expects import (
    be_true,
    expect
)
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
)

# for testing
from .fixtures import katamari

# software under test
from cse_575.data.common import Environment

# Setup
scenarios("../features/environment_loader.feature")

# ********** Keys ********** #
# @scenario('features/environment_loader.feature', 'The environment loader is built')
# def test_the_environment_loader_is_built():
#    """The environment loader is built."""


@given('a built environment loader')
def a_built_environment_loader(katamari):
    katamari.environment = Environment()
    return


@when('the keys are checked')
def the_keys_are_checked(katamari):
    environment = katamari.environment
    expect(environment.raw_data_folder.is_dir()).to(be_true)
    expect(environment.zero_test_images.is_file()).to(be_true)
    expect(environment.one_test_images.is_file()).to(be_true)
    expect(environment.zero_train_images.is_file()).to(be_true)
    expect(environment.one_train_images.is_file()).to(be_true)
    return


@then('it has the expected keys')
def it_has_the_expected_keys():
    return
