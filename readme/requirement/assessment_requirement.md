# Assessment Requirement and Marking Rubric

## Assessment Requirement Related Files

- [MSE800_Assessment1 Requirement](../system_doc/MSE800_Assessment1-V1.md)
- [MSE800_Assessment1 Important Announcement](important_anncouncement.md)
- [MSE800_Assessment1 Blackboard](assessment_requirement_blackboard.md)


## Introduction
For the first assessment, it is an **individual** project. Everyone needs to develop the application using **Python** as per the assessment brief, for the task given in the brief - which is the **Car Rental System**. The submission deadline is **Week 6, Friday (30/Aug/2024) at 11:59 PM**.

## Requirements
### User Management
- **a.** Implement user registration and login functionality.  
- **b.** Differentiate between customer and admin roles, each with specific privileges.

### Car Management
- **c.** Create a database of available cars, including their details (ID, make, model, year, mileage, available now, minimum rent period, maximum rent period).  
- **d.** Allow admins to add, update, and delete car records.

### Rental Booking
- **e.** Enable customers to view available cars and their details.  
- **f.** Implement a booking feature that allows customers to select a car, specify rental dates, and provide necessary details.  
- **g.** Calculate the rental fees based on the selected car, rental duration, and any additional charges.

### Rental Management
- **h.** Allow admins to manage rental bookings, including approving or rejecting requests.

## Important Announcement

### Assessment 1 - MSE800 Software Engineering

> **Notice:** No manual configurations should be needed for running your project!! Please attach `requirements.txt` inside your project!!

## More Details of Assessment 1

- You need to develop a **Command-line User Interface (CUI)** version of the software product using **Python Programming Language**.
- **No limitation** on IDE or database.
- All **Object-Oriented (OO) Programming concepts**, such as encapsulation, abstraction, inheritance, and polymorphism, **must be applied** to your project.
- **At least one** design pattern should be used in your project.
- The program needs to be **bug-free** and has robust error handling.
- The program is easy to compile and run:
  - **Without any manual configurations** (e.g., setup input/output files, import files, etc.).
  - Need a **`requirements.txt`** file including all installed packages inside.


## Marking Rubric

Your assignment will be evaluated based on the following criteria:

### Task 1: Design and Architecture Weighting: 30%

#### User Documentation (10%)
| Criterion | A (80-100)% | B (65-79)% | C (50-64)% | D (40-49)% | E (0-39)% |
|-----------|-------------|------------|------------|------------|-----------|
| **User Documentation** | Provide clear and well-structured ReadMe file that describe the Car Rental System to Users and Programmers. ReadMe file includes ALL of the following: <ul><li>A step-by-step guidance on how to configure, install and operate the Car Rental System</li><li>All relevant files are included. Also explain the purpose of each file in the context of the system</li><li>The ReadMe file clearly states the licensing terms under which the Car Rental System is released.</li><li>Any known bugs or issues with the system should be documented.</li><li>Credit section should include your details as developer of the Car Rental System</li></ul> | Provide clear and well-structured ReadMe file that describe the Car Rental System to Users and Programmers. ReadMe file include the following: <ul><li>A step-by-step guidance on how to configure, install and operate the Car Rental System</li><li>All relevant files are included. Also explain the purpose of each file in the context of the system</li><li>The ReadMe file clearly states the licensing terms under which the Car Rental System is released.</li></ul> | Provide clear and well-structured ReadMe file that describe the Car Rental System to Users and Programmers. ReadMe file include the following: <ul><li>A step-by-step guidance on how to configure, install and operate the Car Rental System</li><li>All relevant files are included. Also explain the purpose of each file in the context of the system</li></ul> | Provide a ReadMe file that does not clearly describe the Car Rental System to Users and Programmers. | The provided ReadMe file does not clearly describe the Car Rental System to users and programmers, lacking essential details and clarity necessary for understanding and utilization. |

#### System Documentation (20%)
| Criterion | A (80-100)% | B (65-79)% | C (50-64)% | D (40-49)% | E (0-39)% |
|-----------|-------------|------------|------------|------------|-----------|
| **System Documentation** | To explain the design and architecture of the system, **ALL** of the following UML diagrams are provided: <ul><li>Class Diagram</li><li>Use Case Diagram</li><li>Sequence Diagram</li></ul> | To explain the design and architecture of the system, **any 2** of the following UML diagrams are provided: <ul><li>Class Diagram</li><li>Use Case Diagram</li><li>Sequence Diagram</li></ul> | To explain the design and architecture of the system, **any 1** of the following UML diagrams are provided: <ul><li>Class Diagram</li><li>Use Case Diagram</li><li>Sequence Diagram</li></ul> | Only one of the following UML diagrams is provided to explain the design and architecture of the system: Class Diagram, Use Case Diagram, or Sequence Diagram, but it is incomplete or unclear, lacking the necessary detail to effectively communicate the system's design and architecture. | No UML diagram is provided to explain the design and architecture of the system, indicating a lack of visual representation to aid in understanding the system's structure and functionality. |

### Task 2: Innovative Solutions Weighting: 40%

#### Car Rental System (30%)
| Criterion | A (80-100)% | B (65-79)% | C (50-64)% | D (40-49)% | E (0-39)% |
|-----------|-------------|------------|------------|------------|-----------|
| **Car Rental System** | The system meets **ALL 4** specified requirements and provides a seamless car rental experience for customers **AND** admins. <br> Include an innovative feature or enhancement that sets your car rental system apart from traditional systems. | The system meets at least **any 3 of the 4** specified requirements and provides a good car rental experience for customers **AND** admins. <br> **Does not include** any innovative feature or enhancement. | The system meets at least **any 2 out of the 4** specified requirements and provides a good car rental experience for **EITHER** customers **OR** admins. | The system meets any **1** of the specified requirements and provides a poor car rental experience for **EITHER** customers **OR** admins. | The system fails to meet any of the specified requirements, providing a poor car rental experience for either customers or admins, or both. |

#### Coding Standard (10%)
| Criterion | A (80-100)% | B (65-79)% | C (50-64)% | D (40-49)% | E (0-39)% |
|-----------|-------------|------------|------------|------------|-----------|
| **Coding Standard** | Demonstrate **ALL** of the following guidelines and conventions: <ul><li>Modularity and Encapsulation</li><li>Performance considerations</li><li>Commenting and Documentation</li><li>Indentation and Formatting</li><li>Naming Conventions</li></ul> | Demonstrate **any 3 to 4** of the following guidelines and conventions: <ul><li>Modularity and Encapsulation</li><li>Performance considerations</li><li>Commenting and Documentation</li><li>Indentation and Formatting</li><li>Naming Conventions</li></ul> | Demonstrate **any 1 to 2** of the following guidelines and conventions: <ul><li>Modularity and Encapsulation</li><li>Performance considerations</li><li>Commenting and Documentation</li><li>Indentation and Formatting</li><li>Naming Conventions</li></ul> | Demonstrate **NONE** of the following guidelines and conventions: <ul><li>Modularity and Encapsulation</li><li>Performance considerations</li><li>Commenting and Documentation</li><li>Indentation and Formatting</li><li>Naming Conventions</li></ul> | The system demonstrates none of the following guidelines and conventions: modularity and encapsulation, performance considerations, commenting and documentation, indentation and formatting, and naming conventions. This indicates a lack of adherence to fundamental principles of software development and professionalism. |

### Task 3: Software Evolution Weighting: 30%

#### Maintenance and Support
| Criterion | A (80-100)% | B (65-79)% | C (50-64)% | D (40-49)% | E (0-39)% |
|-----------|-------------|------------|------------|------------|-----------|
| **Maintenance and Support** | A plan is provided covering **ALL** of the following strategies for: <ul><li>Managing software maintenance</li><li>Versioning</li><li>Backward compatibility</li></ul> | A plan is provided covering **any 2** of the following 3 strategies: <ul><li>Managing software maintenance</li><li>Versioning</li><li>Backward compatibility</li></ul> | A plan is provided covering **any 1** of the following 3 strategies: <ul><li>Managing software maintenance</li><li>Versioning</li><li>Backward compatibility</li></ul> | A plan is provided covering only one of the following strategies: managing software maintenance, versioning, or backward compatibility, but the plan is incomplete or lacks detail, indicating a limited understanding of software management principles. | No plan is provided covering any of the specified strategies: managing software maintenance, versioning, or backward compatibility, indicating a lack of consideration for essential aspects of software development and maintenance. |
