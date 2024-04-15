Feature: Email Subscription

Scenario: Successful email subscription
    Given a user would like to subscribe to an email list
    When the user clicks the subscribe button
    Then the user will continue to receive emails whenever a newsletter is distributed

Scenario: User attempts to subscribe with an invalid email address
    Given a user would like to subscribe to an email list
    When the user enters an invalid email address
    And clicks the subscribe button
    Then an error message should be displayed indicating an invalid email address

Scenario: User attempts to subscribe with an already subscribed email address
    Given a user is already subscribed to the email list
    When the user enters the same email address
    And clicks the subscribe button
    Then a message should be displayed indicating that the email address is already subscribed

Scenario: User unsubscribes from the email list
    Given a user is subscribed to the email list
    When the user clicks the unsubscribe link in a received email
    Then the user should be removed from the email list
    And should no longer receive newsletters

Scenario: User re-subscribes after unsubscribing
    Given a user has previously unsubscribed from the email list
    When the user revisits the subscription page
    And enters their email address
    And clicks the subscribe button
    Then the user should be re-subscribed to the email list
    And should start receiving newsletters again

Scenario: Newsletter distribution to subscribed users
    Given a newsletter is ready to be distributed
    When the newsletter is sent out
    Then all subscribed users should receive the newsletter in their email inbox

Scenario: Newsletter contains an unsubscribe link
    Given a user receives a newsletter email
    When the user opens the email
    Then an unsubscribe link should be visible in the email content
    And clicking the link should allow the user to unsubscribe from the email list