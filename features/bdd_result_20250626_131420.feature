Feature: Automated Test Result

  Scenario: Run through the to-do steps
    Given I am on the Simplified Checkout login page "https://checkout.simplified.ai/"
    And I have valid credentials
    When I enter email "admin@itoolverse.com" in the email field
    And I enter password "zKs4%CzRii&88" in the password field
    And I check the "Remember me" checkbox
    And I click the "Sign in" button
    Then I should be successfully logged into the dashboard
    When I search for "My APP" section
    And I locate the "Simplified Checkout" application
    And I click on the Simplified Checkout app
    Then I should be navigated to the application interface
    When I click on the "Instances" menu from the left-hand side navigation
    And I wait for the page to fully load
    And I click on the "Create Instance" button
    Then I should see the instance creation form/interface

    # Step Results
    # Step 1: N/A [FAILED]
    # Step 2: Navigated to the Simplified Checkout login page. Verdict: Success [PASSED]
    # Step 3: Click on the 'Instances' menu from the left-hand side navigation. Verdict: Success [PASSED]
    # Step 4: Wait for the page to fully load and click on the 'Create Instance' button. Verdict: Success [PASSED]
