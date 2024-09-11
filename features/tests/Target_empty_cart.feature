Feature: Test Scenarios for empty cart functionality

  Scenario: User can clicks on the cart icon and verifies that “Your cart is empty” message
    Given Open Target page
    When Click on Cart icon
    Then Verify message is shown

  Scenario: User can navigate to Sign In page
    Given Open target page
    When Click Sign In
    Then Click on Sign In again
    Then Verify Sign In form opened
