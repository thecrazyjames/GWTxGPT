Sure, here's an example of a Gherkin feature file for a food delivery scenario, following the format provided in the image:

Feature: Food Delivery
  As a customer
  I want to order food online and have it delivered to my address
  So that I can enjoy a meal without leaving my home

  Scenario: Successful food delivery
    Given I am logged in to my account
    And I have selected a restaurant and added items to my cart
    When I proceed to checkout
    And I enter my delivery address and payment details
    And I confirm my order
    Then I should see an order confirmation page
    And I should receive an email with my order details
    And my order should be delivered within the estimated time

  Scenario: Unavailable menu item
    Given I am logged in to my account
    And I have selected a restaurant
    When I try to add an item that is out of stock to my cart
    Then I should see an error message indicating the item is unavailable
    And the out-of-stock item should not be added to my cart

  Scenario: Incorrect delivery address
    Given I am logged in to my account
    And I have items in my cart
    When I proceed to checkout
    And I enter an incorrect or invalid delivery address
    And I try to confirm my order
    Then I should see an error message about the invalid address
    And I should be prompted to enter a valid delivery address

This feature file covers three scenarios: a successful food delivery, handling an unavailable menu item, and dealing with an incorrect delivery address. Each scenario follows the Given-When-Then structure to clearly define the preconditions, actions, and expected outcomes.