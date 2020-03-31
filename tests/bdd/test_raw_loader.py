# coding=utf-8
"""Raw data loader feature tests."""

# pypi
from expects import (
    equal,
    expect,
)
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
)

# software under test
from cse_575.data.loader import RawData

# for testing
from .fixtures import katamari

scenarios("../features/raw_loader.feature")

# ********** Zero Training Images ********** #
#@scenario('features/raw_loader.feature', 'The raw Zero training images are loaded')
#def test_the_raw_zero_training_images_are_loaded():
#    """The raw Zero training images are loaded."""


@given('a raw data loader')
def a_raw_data_loader(katamari):
    katamari.raw_data = RawData()
    return


@when('the zero training images are checked')
def the_zero_training_images_are_checked(katamari):
    katamari.shape = katamari.raw_data.zero_train_images.shape
    katamari.expected_rows = 5923
    return


@then('they are the expected shape')
def they_are_the_expected_shape(katamari):
    expect(katamari.shape[0]).to(equal(28))
    expect(katamari.shape[1]).to(equal(28))
    expect(katamari.shape[2]).to(equal(katamari.expected_rows))
    return

# ********** One images Training ********** #
#  Scenario: The raw one training images are loaded
#    Given a raw data loader


@when("the one training images are checked")
def check_one_training_images(katamari):
    katamari.shape = katamari.raw_data.one_train_images.shape
    katamari.expected_rows = 6742
    return
    
#   Then they are the expected shape

# ********** Zero Test Images ********** #
#  Scenario: The raw Zero test images are loaded
#    Given a raw data loader


@when("the zero test images are checked")
def check_zero_test_images(katamari):
    katamari.shape = katamari.raw_data.zero_test_images.shape
    katamari.expected_rows = 980
    return

#    Then they are the expected shape

# ********** One test images ********** #
#  Scenario: The raw one test images are loaded
#    Given a raw data loader


@when("the one test images are checked")
def check_one_test_images(katamari):
    katamari.shape = katamari.raw_data.one_test_images.shape
    katamari.expected_rows = 1135
    return

#    Then they are the expected shape
