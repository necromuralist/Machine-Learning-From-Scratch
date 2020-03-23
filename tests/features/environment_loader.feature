Feature: Environment Loader
  As a user I want to be able to load environment variables.

  Scenario: The environment loader is built
    Given a built environment loader
    When the keys are checked
    Then it has the expected keys
            
