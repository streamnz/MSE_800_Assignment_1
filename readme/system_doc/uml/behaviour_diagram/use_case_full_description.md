# Car Rental System Use Case Descriptions

## Table of Contents
1. [Register Use Case](#register-use-case)
2. [Login Use Case](#login-use-case)
3. [View Available Cars Use Case](#view-available-cars-use-case)
4. [Book Car Use Case](#book-car-use-case)
5. [View Rental History Use Case](#view-rental-history-use-case)
6. [Manage Cars Use Case](#manage-cars-use-case)
7. [Manage Users Use Case](#manage-users-use-case)
8. [Manage Rentals Use Case](#manage-rentals-use-case)
9. [View Current User Info Use Case](#view-current-user-info-use-case)
10. [View Car Details Use Case](#view-car-details-use-case)
11. [Search Cars Use Case](#search-cars-use-case)
12. [Select Rental Dates Use Case](#select-rental-dates-use-case)
13. [Confirm Booking Use Case](#confirm-booking-use-case)
14. [Approve Booking Use Case](#approve-booking-use-case)
15. [Deny Booking Use Case](#deny-booking-use-case)
16. [View Booking Details Use Case](#view-booking-details-use-case)
17. [Add Car Use Case](#add-car-use-case)
18. [Update Car Use Case](#update-car-use-case)
19. [Delete Car Use Case](#delete-car-use-case)
20. [Add User Use Case](#add-user-use-case)
21. [Update User Use Case](#update-user-use-case)
22. [Delete User Use Case](#delete-user-use-case)
23. [View User Details Use Case](#view-user-details-use-case)

---

### Register Use Case
| **Use Case Name** | Register |
| ----------------- | -------- |
| **Scenario** | Register a new customer account. |
| **Triggering Event** | A new customer wants to create an account to access the car rental service. |
| **Brief Description** | The system allows a customer to create an account by entering basic customer information and then additional details like addresses and payment information. |
| **Actors** | Customer. |
| **Related Use Cases** | Might be invoked by the "Login" use case. |
| **Stakeholders** | Customer Support, Marketing. |
| **Preconditions** | Customer account subsystem must be available. Customer details and authorization services must be available. |
| **Postconditions** | Customer account must be created and saved. Addresses and payment information must be validated. The customer account must be associated with the addresses and payment information. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer indicates a desire to register an account by providing basic details. | 1.1 System checks for the availability of the customer account subsystem. 1.2 System prompts for additional customer details. |
| 2. Customer provides address details. | 2.1 System validates the provided address information. 2.2 System associates the address with the customer account. |
| 3. Customer enters payment information. | 3.1 System validates the payment information. 3.2 System stores the payment information securely. 3.3 System confirms the account creation with all associated details. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Basic customer information is incomplete. | Prompt the customer to enter all required fields. |
| 2.1 The provided address is invalid. | Notify the customer and request a valid address. |
| 3.1 The payment information is invalid. | Prompt the customer to re-enter or correct payment details. |

### Login Use Case
| **Use Case Name** | Login |
| ----------------- | ------ |
| **Scenario** | Customer/Admin logs into the system. |
| **Triggering Event** | A customer/admin wants to access the system using their credentials. |
| **Brief Description** | The system allows a user to log in by entering a valid username and password. |
| **Actors** | Customer, Admin. |
| **Related Use Cases** | Might be invoked by the "Register" use case for new users. |
| **Stakeholders** | System Administrators. |
| **Preconditions** | User account must exist, and the login subsystem must be available. |
| **Postconditions** | User is authenticated and granted access to the system's functionalities based on their role. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. User enters their username and password. | 1.1 System validates the credentials against the stored user data. |
| 2. User selects login. | 2.1 If credentials are valid, system grants access to the user's dashboard. 2.2 If credentials are invalid, system displays an error message. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Credentials do not match any existing account. | Display an error message and prompt for re-entry. |


### View Available Cars Use Case
| **Use Case Name** | View Available Cars |
| ----------------- | ------------------- |
| **Scenario** | Customer views the list of available cars for rental. |
| **Triggering Event** | A customer wants to browse available cars before booking. |
| **Brief Description** | The system displays a list of cars that are available for rental, along with their details. |
| **Actors** | Customer. |
| **Related Use Cases** | Might be invoked by the "Book Car" use case. |
| **Stakeholders** | Marketing, Customer Support. |
| **Preconditions** | Car inventory data must be available and up-to-date. |
| **Postconditions** | The list of available cars is displayed to the customer. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer selects to view available cars. | 1.1 System retrieves the list of available cars from the inventory. 1.2 System displays the car details to the customer. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 No cars are available for the selected date range. | Display a message indicating that no cars are available. |

### Book Car Use Case
| **Use Case Name** | Book Car |
| ----------------- | -------- |
| **Scenario** | Customer books a car for a specified period. |
| **Triggering Event** | A customer decides to rent a car after viewing available options. |
| **Brief Description** | The system allows the customer to select a car, specify rental dates, and confirm the booking. |
| **Actors** | Customer. |
| **Related Use Cases** | "View Available Cars" use case. |
| **Stakeholders** | Sales, Customer Support. |
| **Preconditions** | Customer must be logged in, and the selected car must be available. |
| **Postconditions** | Booking is confirmed, and the car is reserved for the specified dates. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer selects a car to book. | 1.1 System retrieves the car's availability. |
| 2. Customer selects rental dates. | 2.1 System verifies the car's availability for the selected dates. |
| 3. Customer confirms the booking. | 3.1 System reserves the car and updates the booking status. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 The selected car is no longer available. | Notify the customer and suggest alternative cars. |

### View Rental History Use Case
| **Use Case Name** | View Rental History |
| ----------------- | ------------------- |
| **Scenario** | Customer views their rental history. |
| **Triggering Event** | A customer wants to review their past rentals. |
| **Brief Description** | The system displays the history of all rentals made by the customer. |
| **Actors** | Customer. |
| **Related Use Cases** | None. |
| **Stakeholders** | Customer Support. |
| **Preconditions** | Customer must be logged in. |
| **Postconditions** | The rental history is displayed to the customer. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer selects to view rental history. | 1.1 System retrieves the rental history from the database. 1.2 System displays the rental history to the customer. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 No rental history available. | Display a message indicating no past rentals. |

### Manage Cars Use Case
| **Use Case Name** | Manage Cars |
| ----------------- | ----------- |
| **Scenario** | Admin manages the car inventory. |
| **Triggering Event** | An admin wants to add, update, or delete car information. |
| **Brief Description** | The system allows the admin to manage car details in the inventory. |
| **Actors** | Admin. |
| **Related Use Cases** | None. |
| **Stakeholders** | Operations, Inventory Management. |
| **Preconditions** | Admin must be logged in, and the car inventory subsystem must be available. |
| **Postconditions** | The car details are updated in the inventory. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects to manage cars. | 1.1 System displays the car management options (Add, Update, Delete). |
| 2. Admin adds/updates/deletes car information. | 2.1 System updates the car inventory accordingly. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Invalid car details provided. | Prompt the admin to correct the information. |

### Manage Users Use Case
| **Use Case Name** | Manage Users |
| ----------------- | ------------ |
| **Scenario** | Admin manages user accounts. |
| **Triggering Event** | An admin wants to add, update, or delete user information. |
| **Brief Description** | The system allows the admin to manage user details, including adding new users or modifying existing ones. |
| **Actors** | Admin. |
| **Related Use Cases** | None. |
| **Stakeholders** | Human Resources, Customer Support. |
| **Preconditions** | Admin must be logged in. |
| **Postconditions** | User accounts are updated in the system. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects to manage users. | 1.1 System displays the user management options (Add, Update, Delete). |
| 2. Admin adds/updates/deletes user information. | 2.1 System updates the user account details accordingly. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Invalid user details provided. | Prompt the admin to correct the information. |

### Manage Rentals Use Case
| **Use Case Name** | Manage Rentals |
| ----------------- | -------------- |
| **Scenario** | Admin manages car rental bookings. |
| **Triggering Event** | An admin wants to approve, deny, or view booking details. |
| **Brief Description** | The system allows the admin to manage rental bookings, including approving or denying them. |
| **Actors** | Admin. |
| **Related Use Cases** | None. |
| **Stakeholders** | Sales, Customer Support. |
| **Preconditions** | Admin must be logged in, and booking data must be available. |
| **Postconditions** | Booking statuses are updated in the system. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects to manage rentals. | 1.1 System displays the rental management options (Approve, Deny, View Details). |
| 2. Admin approves/denies a booking or views booking details. | 2.1 System updates the booking status accordingly or displays the booking details. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Invalid booking details provided. | Prompt the admin to correct the information. |

### View Current User Info Use Case
| **Use Case Name** | View Current User Info |
| ----------------- | ---------------------- |
| **Scenario** | Customer views their account information. |
| **Triggering Event** | A customer wants to review their personal account details. |
| **Brief Description** | The system displays the current user’s account information, such as personal details and rental history. |
| **Actors** | Customer. |
| **Related Use Cases** | None. |
| **Stakeholders** | Customer Support. |
| **Preconditions** | Customer must be logged in. |
| **Postconditions** | The account information is displayed to the customer. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer selects to view current user info. | 1.1 System retrieves the user's account information from the database. 1.2 System displays the account information to the customer. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 No account information found. | Display a message indicating no account details are available. |

### View Car Details Use Case
| **Use Case Name** | View Car Details |
| ----------------- | ---------------- |
| **Scenario** | Customer/Admin views detailed information about a specific car. |
| **Triggering Event** | A customer/admin selects a car to view its details. |
| **Brief Description** | The system displays detailed information about the selected car, including make, model, year, and rental status. |
| **Actors** | Customer, Admin. |
| **Related Use Cases** | "View Available Cars" and "Manage Cars". |
| **Stakeholders** | Inventory Management, Marketing. |
| **Preconditions** | Car details must be available in the system. |
| **Postconditions** | The detailed car information is displayed. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. User selects a car to view details. | 1.1 System retrieves and displays detailed information about the car. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Car details are not found. | Notify the user that details are unavailable. |

### Search Cars Use Case
| **Use Case Name** | Search Cars |
| ----------------- | ----------- |
| **Scenario** | Customer searches for cars based on specific criteria. |
| **Triggering Event** | A customer wants to find a car that meets specific requirements, such as make, model, or availability. |
| **Brief Description** | The system allows the customer to search the car inventory based on various criteria. |
| **Actors** | Customer. |
| **Related Use Cases** | "View Available Cars". |
| **Stakeholders** | Marketing, Inventory Management. |
| **Preconditions** | Car inventory data must be available. |
| **Postconditions** | A list of cars matching the search criteria is displayed. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer enters search criteria. | 1.1 System searches the inventory and retrieves matching cars. 1.2 System displays the search results. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 No cars match the search criteria. | Display a message indicating no cars were found. |


### Select Rental Dates Use Case
| **Use Case Name** | Select Rental Dates |
| ----------------- | ------------------- |
| **Scenario** | Customer selects the start and end dates for renting a car. |
| **Triggering Event** | A customer decides to book a car and needs to select the rental period. |
| **Brief Description** | The system allows the customer to select the desired rental dates for a specific car. |
| **Actors** | Customer. |
| **Related Use Cases** | "Book Car". |
| **Stakeholders** | Operations. |
| **Preconditions** | Car must be available for the selected dates. |
| **Postconditions** | Rental dates are confirmed and saved for the booking. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer selects rental start and end dates. | 1.1 System checks the car's availability for the selected dates. 1.2 If available, system confirms the selection. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 The car is not available for the selected dates. | Notify the customer and suggest alternative dates or cars. |

### Confirm Booking Use Case
| **Use Case Name** | Confirm Booking |
| ----------------- | --------------- |
| **Scenario** | Customer confirms the booking of a car. |
| **Triggering Event** | A customer decides to confirm the car rental after selecting the car and rental dates. |
| **Brief Description** | The system allows the customer to confirm the booking, finalizing the rental. |
| **Actors** | Customer. |
| **Related Use Cases** | "Book Car", "Select Rental Dates". |
| **Stakeholders** | Sales, Operations. |
| **Preconditions** | Car must be available, and rental dates must be selected. |
| **Postconditions** | The booking is confirmed, and the car is reserved. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Customer confirms the booking. | 1.1 System finalizes the booking, updates the inventory, and sends a confirmation to the customer. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 An error occurs during booking confirmation. | Notify the customer of the error and attempt to resolve it. |

### Approve Booking Use Case
| **Use Case Name** | Approve Booking |
| ----------------- | --------------- |
| **Scenario** | Admin approves a car rental booking. |
| **Triggering Event** | An admin receives a booking request and needs to approve it. |
| **Brief Description** | The system allows the admin to approve a booking, confirming the rental. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Rentals". |
| **Stakeholders** | Sales, Customer Support. |
| **Preconditions** | Booking request must exist and be valid. |
| **Postconditions** | The booking is approved, and the car is reserved for the customer. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects to approve a booking. | 1.1 System confirms the booking and updates the rental status. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 The booking request is invalid. | Notify the admin and request further action. |

### Deny Booking Use Case
| **Use Case Name** | Deny Booking |
| ----------------- | ------------- |
| **Scenario** | Admin denies a car rental booking. |
| **Triggering Event** | An admin receives a booking request and needs to deny it. |
| **Brief Description** | The system allows the admin to deny a booking request, canceling the rental. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Rentals". |
| **Stakeholders** | Sales, Customer Support. |
| **Preconditions** | Booking request must exist and be valid. |
| **Postconditions** | The booking is denied, and the car is made available again. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects to deny a booking. | 1.1 System cancels the booking and updates the inventory. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 The booking request is invalid. | Notify the admin and request further action. |

### View Booking Details Use Case
| **Use Case Name** | View Booking Details |
| ----------------- | -------------------- |
| **Scenario** | Admin views the details of a car rental booking. |
| **Triggering Event** | An admin wants to see the details of a specific booking. |
| **Brief Description** | The system displays the detailed information of a specific booking to the admin. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Rentals". |
| **Stakeholders** | Customer Support, Sales. |
| **Preconditions** | Booking details must be available. |
| **Postconditions** | The booking details are displayed to the admin. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects to view booking details. | 1.1 System retrieves and displays the booking details from the database. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Booking details are not found. | Notify the admin that booking details are unavailable. |

### Add Car Use Case
| **Use Case Name** | Add Car |
| ----------------- | ------- |
| **Scenario** | Admin adds a new car to the inventory. |
| **Triggering Event** | An admin wants to add a new car to the car rental inventory. |
| **Brief Description** | The system allows the admin to input car details and add a new car to the system. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Cars". |
| **Stakeholders** | Inventory Management, Operations. |
| **Preconditions** | The car inventory subsystem must be available. |
| **Postconditions** | The car is added to the inventory and made available for booking. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin enters car details. | 1.1 System validates the car information. 1.2 System adds the car to the inventory and updates the available cars list. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Invalid car details provided. | Prompt the admin to correct the information. |

### Update Car Use Case
| **Use Case Name** | Update Car |
| ----------------- | --------- |
| **Scenario** | Admin updates car details in the inventory. |
| **Triggering Event** | An admin wants to update the information of an existing car in the inventory. |
| **Brief Description** | The system allows the admin to modify the details of an existing car in the system. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Cars". |
| **Stakeholders** | Inventory Management, Operations. |
| **Preconditions** | The car must exist in the inventory. |
| **Postconditions** | The car details are updated in the system. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects a car to update. | 1.1 System retrieves the current details of the car. 1.2 System allows the admin to update the car details. 1.3 System saves the updated car information. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Invalid car details provided. | Prompt the admin to correct the information. |

###  Delete Car Use Case
| **Use Case Name** | Delete Car |
| ----------------- | ---------- |
| **Scenario** | Admin removes a car from the inventory. |
| **Triggering Event** | An admin wants to delete a car from the car rental inventory. |
| **Brief Description** | The system allows the admin to remove a car from the system, making it unavailable for future rentals. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Cars". |
| **Stakeholders** | Inventory Management, Operations. |
| **Preconditions** | The car must exist in the inventory. |
| **Postconditions** | The car is removed from the inventory and no longer available for booking. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects a car to delete. | 1.1 System retrieves the current details of the car. 1.2 System removes the car from the inventory. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 The car cannot be deleted if it has active rentals. | Notify the admin and suggest deactivating the car instead. |

### Add User Use Case
| **Use Case Name** | Add User |
| ----------------- | -------- |
| **Scenario** | Admin adds a new user account to the system. |
| **Triggering Event** | An admin wants to create a new user account. |
| **Brief Description** | The system allows the admin to input user details and add a new user account. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Users". |
| **Stakeholders** | Human Resources, Customer Support. |
| **Preconditions** | The user management subsystem must be available. |
| **Postconditions** | The user account is created and saved in the system. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin enters user details. | 1.1 System validates the user information. 1.2 System creates the user account in the system. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Invalid user details provided. | Prompt the admin to correct the information. |

### Update User Use Case
| **Use Case Name** | Update User |
| ----------------- | ----------- |
| **Scenario** | Admin updates a user's account information. |
| **Triggering Event** | An admin wants to update the details of an existing user account. |
| **Brief Description** | The system allows the admin to modify the details of an existing user account. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Users". |
| **Stakeholders** | Human Resources, Customer Support. |
| **Preconditions** | The user must have an existing account in the system. |
| **Postconditions** | The user account details are updated in the system. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects a user to update. | 1.1 System retrieves the current details of the user. 1.2 System allows the admin to update the user details. 1.3 System saves the updated user information. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 Invalid user details provided. | Prompt the admin to correct the information. |

### Delete User Use Case
| **Use Case Name** | Delete User |
| ----------------- | ----------- |
| **Scenario** | Admin deletes a user account from the system. |
| **Triggering Event** | An admin wants to remove a user account from the system. |
| **Brief Description** | The system allows the admin to delete a user account, making it inactive in the system. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Users". |
| **Stakeholders** | Human Resources, Customer Support. |
| **Preconditions** | The user must have an existing account in the system. |
| **Postconditions** | The user account is removed from the system. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects a user to delete. | 1.1 System retrieves the current details of the user. 1.2 System deactivates the user account in the system. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 The user cannot be deleted if they have active rentals or dependencies. | Notify the admin and suggest deactivating the account instead. |

### View User Details Use Case
| **Use Case Name** | View User Details |
| ----------------- | ----------------- |
| **Scenario** | Admin views the details of a user account. |
| **Triggering Event** | An admin wants to see the details of a specific user account. |
| **Brief Description** | The system displays the detailed information of a specific user to the admin. |
| **Actors** | Admin. |
| **Related Use Cases** | "Manage Users". |
| **Stakeholders** | Human Resources, Customer Support. |
| **Preconditions** | User details must be available in the system. |
| **Postconditions** | The user details are displayed to the admin. |
| **Flow of Activities** | **Actor's Actions** | **System's Responsibilities** |
| ---------------------- | ------------------- | ---------------------------- |
| 1. Admin selects to view user details. | 1.1 System retrieves and displays the user details from the database. |
| **Exception Conditions** | **System Response** |
| ------------------------ | ------------------- |
| 1.1 User details are not found. | Notify the admin that user details are unavailable. |

