Feature: Edit driver
  In order to keep updated my previous registers about drivers,
  As a user,
  I want to edit a driver register I created.

  Background: There are registered 2 users but only 1 driver registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists driver registered by "user1"
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 31  | Finland     | Mercedes | 1.73 m | 69 kg  |
    And Exists driver registered by "user1"


  Scenario: Edit owned driver (have to edit all fields)
    Given I login as a user "user1" with password "password1"
    When  I view the details for driver "Portimao"
    And I edit current driver
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 32  | Finland     | Mercedes | 1.73 m | 69 kg  |
    Then I'm viewing the details page for driver "Portimao" by "user1"
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 32  | Finland     | Mercedes | 1.73 m | 69 kg  |
    And there's 1 driver

  Scenario: Try to edit not owned driver
    Given I login as a user "user2" with password "password2"
    When  I view the details for driver "Valteri Bottas"
    Then ther's no "edit" link available

  Scenario: Force edit driver but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the driver with name "Valtteri Bottas"
      | name            | age | nationality | scuderia | height | weight |
      | Valtteri Bottas | 31  | Finland     | Williams | 1.73 m | 69 kg  |
    Then Server responds with page containing "403 Forbidden"