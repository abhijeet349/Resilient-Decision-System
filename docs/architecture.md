# System Architecture

Client Request
      |
      v
FastAPI API Layer
      |
      v
Workflow Engine
      |
      v
Rule Engine
      |
      v
SQLite Database
      |
      v
Audit Logs

## Components

API Layer
Handles incoming requests.

Rule Engine
Evaluates configurable rules from config.json.

Workflow Engine
Runs workflow stages and handles retry logic.

Database
Stores workflow state and audit logs.

Audit Logging
Tracks decisions for traceability.
