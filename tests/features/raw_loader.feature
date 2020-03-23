Feature: Raw data loader
  As a user I want to be able to load the raw data.

  Scenario: The raw Zero training images are loaded
    Given a raw data loader
    When the zero training images are checked
    Then they are the expected shape
