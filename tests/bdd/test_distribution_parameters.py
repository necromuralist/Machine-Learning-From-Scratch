# coding=utf-8
"""A data distribution parameters extractor feature tests."""

# from pypi
from expects import (
    be_true,
    equal,
    expect
)

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
)

# testing setup
from .fixtures import katamari
scenarios("../features/distribution_parameters.feature")

and_also = then

# software under test
from cse_575.data.loader import RawData
from cse_575.data.statistics import TheStatistician

# ********** The flattened data ********** #
#@scenario('features/distribution_parameters.feature', 'The data is flattened.')
#def test_the_data_is_flattened():
#    """The data is flattened.."""


@given('a data parameters object with zero training data')
def a_data_parameters_object_with_zero_training_data(katamari):
    katamari.raw_data = RawData()
    katamari.parameters = TheStatistician(
        katamari.raw_data.zero_train_images)
    return


@when('the flattened data is checked')
def the_flattened_data_is_checked(katamari):
    katamari.flattened = katamari.parameters.flattened
    return

@then("it has the expected shape")
def check_shape(katamari):
    raw_data = katamari.raw_data.zero_train_images
    expect(len(katamari.flattened)).to(equal(raw_data.shape[-1]))
    return


@and_also('it is the expected flattened data')
def it_is_the_expected_flattened_data(katamari):
    for row in range(len(katamari.flattened)):
        expected = katamari.raw_data.zero_train_images[:, :, row].flatten()
        actual = katamari.flattened[row]
        expect(all(expected==actual)).to(be_true)
    return

# ********** Means ********** #
#  Scenario: The means are calculated
#    Given a data parameters object with zero training data


@when("the means are checked")
def check_means(katamari):
    katamari.actual = katamari.parameters.means
    return


@then("they are the expected means")
def check_values(katamari):
    for row in range(len(katamari.parameters.flattened)):
        expected = katamari.raw_data.zero_train_images[:, :, row].mean()
        actual = katamari.actual[row]
        expect(actual).to(equal(expected))
    return

# ********** Variance ********** #
#  Scenario: The variances are calculated
#    Given a data parameters object with zero training data


@when("the variances are checked")
def check_variances(katamari):
    katamari.actual = katamari.parameters.variances
    return


@then("they are the expected variances")
def expect_variances(katamari):
    for row in range(len(katamari.parameters.flattened)):
        expected = katamari.raw_data.zero_train_images[:, :, row].var(
            axis=1).mean(axis=0)
        actual = katamari.actual[row]
        expect(actual).to(equal(expected))
    return
