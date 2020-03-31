Feature: A data distribution parameters extractor
  As a user, I want to be able to find the parameters for the distribution of the data representing each image.

  Scenario: The data is flattened
    Given a data parameters object with zero training data
    When the flattened data is checked
    Then it has the expected shape
    And it is the expected flattened data
    
  Scenario: The means are calculated
    Given a data parameters object with zero training data
    When the means are checked
    Then they are the expected means
                
  Scenario: The variances are calculated
    Given a data parameters object with zero training data
    When the variances are checked
    Then they are the expected variances
