@basketWithPromotions
Feature: Basket with promotions


  @LoginWithRandomUserAtg
  Scenario: Add products to basket (precondition)
    And I choose addtobasketapi service
    And I set JSESSIONID stored as cookie to header
    And I set field productId to xprod40022 in request body
    And I set field quantity to 2 in request body
    And I send request parameters to body
    When I send POST request
    Then response code should be 200
    And response body should be valid json
    And response body is according to schema file successful_AddingToBasketResponse.json
    And I store the value of body path itemId as itemIdValue in global scope

  Scenario: Get promotion discount 10% for order which cost more than 100 UAH (happy path)
    When I choose basketapi service
    And I set JSESSIONID stored as cookie to header
    And I send GET request
    Then response code should be 200
    And response body should be valid json
    And response body is according to schema file basketWithPromotionsResponse.json
    And The response field items[0].id should be equal value of parameter itemIdValue in global scope
    And response field promotions[0].description should be equal 10% discount on an order
    And I store the value of body path amounts.subtotal as subtotal in global scope
    And I multiply first operand subtotal with second operand 0.1 and store result as calculationResult in global scope
    And I subtract first operand subtotal with second operand calculationResult and store result as calculationResult in global scope
    And The response field amounts.total should be equal value of parameter calculationResult in global scope

  Scenario: Remove item from basket (precondition)
    When I choose removeitemfrombasketapi service
    And I set JSESSIONID stored as cookie to header
    And I set parameter itemIdValue to base url
    And I send DELETE request
    Then response code should be 204

  Scenario Outline: Get 20 UAH when ordered a complex lunch including items from first course, second course and drink (happy path)
    And I choose addtobasketapi service
    And I set JSESSIONID stored as cookie to header
    And I set field '<key>' to '<value>' in request body
    And I set field '<quantityKey>' to '<quantityValue>' in request body
    And I send request parameters to body
    When I send POST request
    Then response code should be 200
    And response body should be valid json
    And response body is according to schema file successful_AddingToBasketResponse.json
    And I store the value of body path '<itemId>' as '<itemIdValue>' in global scope
    When I choose basketapi service
    And I set JSESSIONID stored as cookie to header
    And I send GET request
    Then response code should be 200
    And response body should be valid json
    And response body is according to schema file basketWithPromotionsResponse.json
    And The response field items[0].id should be equal value of parameter itemIdValue1 in global scope
    And The response field items[1].id should be equal value of parameter itemIdValue2 in global scope
    And The response field items[2].id should be equal value of parameter itemIdValue3 in global scope
    And I store the value of body path amounts.subtotal as subtotal in global scope
    And I store the value of body path promotions[0].amount as amount in global scope
    And I divide first operand 2000 with second operand subtotal and store result as discountPercent in global scope
    And I round up discountPercent value with scale 0 and rounding mode ROUND_HALF_UP
    And The response field promotions[0].description should contain value of parameter discountPercent in global scope
    And I subtract first operand subtotal with second operand amount and store result as calculationResult in global scope
    And The response field amounts.total should be equal value of parameter calculationResult in global scope

    Examples:
    | key        | value     | quantityKey | quantityValue| itemId | itemIdValue |
    | productId  | prod40021 | quantity    | 1            | itemId | itemIdValue1|
    | productId  | prod60044 | quantity    | 1            | itemId | itemIdValue2|
    | productId  | prod60032 | quantity    | 1            | itemId | itemIdValue3|
