Feature: Test Scenarios for empty cart functionality

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open Target page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

