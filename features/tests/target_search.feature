# Created by Shuchita at 9/13/2024
Feature: Test Scenarios for main page

  Scenario: User can search for product
    Given Open Target main page
    When Search for tea
    Then Verify that correct search result shown for tea

  Scenario: Add any product into the cart
    Given Open Target main page
    When Search for coffee
    And click on the cart button
    And confirm add to cart from the side navigation
    And click cart & check out
    Then verify cart has 1 item(s)


  Scenario: Verify search results have product name and image
    Given Open Target main page
    When Search for bread
    Then Verify each product with a name and an image


