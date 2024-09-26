Feature: Test Scenarios for empty cart functionality

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open Target page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: User can navigate to Sign In page
    Given Open target page
    When Click Sign In
    Then Click on Sign In again
    Then Verify Sign In form opened
