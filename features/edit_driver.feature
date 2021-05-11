Feature: Edit driver
  In order to keep updated my previous registers about drivers,
  As a user,
  I want to edit a driver register I created.

  Background: There are registered 2 users but only 1 driver registered
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists driver registered by "user1"
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 31  | Finland     | Mercedes | 1.73   | 69     |



  Scenario: Edit owned driver
    Given I login as a user "user1" with password "password"
    When  I edit the driver with name "Valtteri Bottas"
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 32  | Finland     | Mercedes | 1.73   | 69     |
    Then I'm viewing the details page for driver by "user1"
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 32  | Finland     | Mercedes | 1.73   | 69     |
    And There is 1 driver

  Scenario: Try to edit not owned driver
    Given I login as a user "user2" with password "password"
    When  I view the details for driver "Valtteri Bottas"
    Then There is no "edit" link available

  Scenario: Force edit driver but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the driver with name "Valtteri Bottas"
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 31  | Finland     | Williams | 1.73   | 69     |
    Then Server responds with page containing "403 Forbidden"