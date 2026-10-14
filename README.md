# probatabankproject
PróbataBank is a modular, terminal-based banking application simulacrum built with Python.
Its architecture prioritizes modularity, data integrity, traceability, and long-term extensibility.

The g foundation consists of a Textual-based terminal interface, reusable input validators and an initial SQLite schema for user identity, profiles and change history.

The long-term goal is to turn these foundations into a cohesive application in which registration, authentication, user data, account management and transaction workflows operate as independent but connected parts of the same system.

Next goal: Build a working interface with 3 working flows
- Register
- Login
- Password recovery

At first with mock data or a direct connection to the sqlite DB created by the `db_creation.py`