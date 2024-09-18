                                        CosmeticsShop System Design Principles
The CosmeticsShop system is designed with the following six software design principles in mind to ensure maintainability, flexibility, and scalability.

1. Single Responsibility Principle (SRP)
Each module or class in the CosmeticsShop system has a single reason to change, which is to manage either products, customers, or purchases. This principle ensures that each class or module has a single, well-defined responsibility, making it easier to maintain and extend the system.

2. Keep It Simple, Stupid (KISS)
The CosmeticsShop system avoids unnecessary complexity by using simple, intuitive data structures and algorithms to manage products, customers, and purchases. This principle encourages simplicity and readability in the code, making it easy to understand and modify.

3. Don't Repeat Yourself (DRY)
The CosmeticsShop system extracts common functionality into reusable methods to avoid duplicated code and improve maintainability. For example, the generate_product_id method is a reusable function that can be used throughout the system, reducing code duplication and making maintenance easier.

4. Open-Closed Principle (OCP)
The CosmeticsShop system is designed to allow new features or functionality to be added without modifying the existing codebase. This principle ensures that the system is flexible and can be extended without breaking existing functionality.

5. Interface Segregation Principle (ISP)
The CosmeticsShop system designs interfaces that are client-specific, rather than general-purpose, to avoid forcing clients to depend on interfaces they don't use. This principle helps reduce coupling and makes the system more modular.

6. Separation of Concerns (SoC)
The CosmeticsShop system separates concerns into distinct modules or layers, each responsible for a specific aspect of the system, to improve maintainability and scalability. For example, the system can be separated into three layers: a presentation layer (handling user input and output), a business logic layer (managing products, customers, and purchases), and a data storage layer (storing and retrieving data).

By following these six software design principles, the CosmeticsShop system is designed to be more maintainable, flexible, and scalable.