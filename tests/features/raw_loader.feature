Feature: Raw data loader
  As a user I want to be able to load the raw data.

  Scenario: The raw Zero training images are loaded
    Given a raw data loader
    When the zero training images are checked
    Then they are the expected shape

  Scenario: The raw one training images are loaded
    Given a raw data loader
    When the one training images are checked
    Then they are the expected shape

  Scenario: The raw Zero test images are loaded
    Given a raw data loader
    When the zero test images are checked
    Then they are the expected shape
    
  Scenario: The raw one test images are loaded
    Given a raw data loader
    When the one test images are checked
    Then they are the expected shape
