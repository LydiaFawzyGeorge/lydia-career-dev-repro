Feature: I want to login after register

 Scenario Outline: Check login
 Given I am on login page
 When I fill in user email <email>
 And I fill in user password <password>
 And I press "Login"
 Then I should see "Log Out" button

  Examples:
  | email                  | password |
  | gApJkTkGkY@mail.com    | JSFkkLxQNo8027632981      |



