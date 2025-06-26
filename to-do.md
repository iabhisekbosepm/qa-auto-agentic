Feature: xyz Checkout Instance Management
  As a registered user
  I want to create a new instance in xyz Checkout
  So that I can manage my checkout configurations

  Background:
    Given the user has valid credentials
    And the xyz Checkout application is available

  @smoke @login @instance-creation
  Scenario: Successfully create a new instance in xyz Checkout
    Given I navigate to "https://checkout.XYZ.ai/"
    When I enter x_Email in the email field
    And I enter x_Password in the password field
    And I check the "Remember me" checkbox
    And I click the "Sign in" button
    Then I should be successfully logged into the dashboard
    And I should see the main application interface

    When I search for the "My APP" section
    And I locate the "xyz Checkout" application
    And I click on the "xyz Checkout" app
    Then I should be redirected to the xyz Checkout interface
    And the application should load completely

    When I click on the "Instances" menu item in the left navigation
    And I wait for the instances page to load completely
    And I click on the "Create Instance" button
    Then I should see the instance creation form
    And all required fields should be visible
    And the form should be ready for input

  @negative @login
  Scenario: Login failure with invalid credentials
    Given I navigate to "https://checkout.xyz.ai/"
    When I enter "invalid@email.com" in the email field
    And I enter "wrongpassword" in the password field
    And I click the "Sign in" button
    Then I should see an error message
    And I should remain on the login page

  @edge-case @navigation
  Scenario: Handle case when xyz Checkout app is not found
    Given I navigate to "https://checkout.xyz.ai/"
    And I login with valid credentials
    When I search for the "My APP" section
    But the "xyz Checkout" application is not visible
    Then I should see a message indicating no apps are available
    Or I should see an option to install the application

  @accessibility @ui
  Scenario: Verify accessibility and UI elements
    Given I navigate to "https://checkout.xyz.ai/"
    When I examine the login page
    Then all form fields should have proper labels
    And the "Sign in" button should be accessible via keyboard
    And the "Remember me" checkbox should be properly labeled
    And the page should have appropriate ARIA attributes

  # Data-driven test scenarios
  @data-driven
  Scenario Outline: Test login with different credential combinations
    Given I navigate to "https://checkout.xyz.ai/"
    When I enter "<email>" in the email field
    And I enter "<password>" in the password field
    And I click the "Sign in" button
    Then I should see "<expected_result>"



  @performance @load-time
  Scenario: Verify page load performance
    Given I navigate to "https://checkout.xyz.ai/"
    When I login with valid credentials
    And I navigate to the "xyz Checkout" app
    And I click on the "Instances" menu
    Then the page should load within 5 seconds
    And all interactive elements should be responsive

  @security @session
  Scenario: Verify remember me functionality
    Given I navigate to "https://checkout.xyz.ai/"
    When I login with valid credentials
    And I check the "Remember me" checkbox
    And I close the browser
    And I reopen the browser
    And I navigate to "https://checkout.xyz.ai/"
    Then I should remain logged in
    And I should see the dashboard without re-entering credentials

  @cleanup
  Scenario: Test cleanup and logout
    Given I am logged into the xyz Checkout application
    When I complete my instance creation tasks
    Then I should be able to logout successfully
    And my session should be properly terminated