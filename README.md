#Policy-Aware Access Control (PAAC) Project

##Overview
The Policy-Aware Access Control (PAAC) project is a Django-based system designed to enforce fine-grained access control using policies, roles, and conditions. This project has been developed as a learning journey to strengthen my backend skills, explore Django REST Framework, and implement robust access control logic with multiple interconnected apps.

##Key Highlights:
Built multiple Django apps for modularity: identity_app, policy_engine, decision_engine, audit_log, and simulation_mode.
Implemented JWT-based authentication with role-based permissions.
Learned advanced DRF concepts such as custom serializers, pagination, nested serializers, and object-level permissions.
Developed a dynamic policy evaluation engine that matches user attributes with policy conditions.
Integrated audit logging and simulation functionality to analyze access control decisions.
Applied real-world design patterns to connect multiple apps cohesively.

##Project Structure
paac_project/
├── identity_app/
│   ├── models.py           # Custom User model with roles, departments, and trust_score
│   ├── views.py            # CRUD views for User management
│   ├── serializers.py      # User_Serializer
│   ├── permissions.py      # Role-based access control logic
│   └── urls.py             # API endpoints for users & JWT
├── policy_engine/
│   ├── models.py           # Policy model with JSON-based conditions
│   ├── views.py            # CRUD views for policies
│   ├── serializers.py      # Policy_Serializer with validation
│   ├── permissions.py      # CEO-only creation, flexible read permissions
│   └── urls.py             # API endpoints for policies
├── decision_engine/
│   ├── models.py           # Decision model to track policy evaluation
│   ├── views.py            # Views to create and list decisions
│   ├── serializers.py      # Decision_Serializer with nested user/policy
│   ├── logic.py            # Policy evaluation & user evaluation logic
│   └── urls.py             # API endpoints for decisions
├── audit_log/
│   ├── models.py           # Audit model to track decision logs
│   ├── views.py            # Views to list audits by user or policy
│   ├── serializers.py      # Audit_Serializer with nested decisions
│   ├── permissions.py      # Auditor and CEO access
│   └── urls.py             # API endpoints for audits
├── simulation_mode/
│   ├── models.py           # Simulation model to simulate decisions for a user
│   ├── views.py            # Views to simulate and list simulations
│   ├── serializers.py      # Simulation_Serializer with validations
│   └── urls.py             # API endpoints for simulation
├── paac_project/            # Django project settings
├── manage.py


##Features

###Identity App
Custom User model with roles (ceo, manager, employee, intern, auditor) and departments.
Full CRUD operations for users.
Role-based permissions for access control.
Pagination for listing users.
Policy Engine
CRUD for policies with priority, effect (allow/deny), action, and resource type.
JSON-based conditions to define which users the policy applies to.
Server-side validation for policy attributes.
Role-based access: CEO can manage policies; managers and auditors can view.

###Decision Engine
Evaluates access requests based on user attributes and policies.
Stores decisions in the database with reasons.
Nested serializers include full user and policy information.
Pagination for listing decisions.

###Audit Log
Tracks all decisions with timestamps.
Filters audits by user or policy.
Access restricted to auditors and CEO.

###Simulation Mode
Simulates access decisions for users before applying policies.
Prevents self-simulation.
Supports role-based access to simulations.
Integrated with the decision evaluation engine.

##Learning Outcomes
Built and integrated five distinct apps with complex relationships.
Applied role-based and object-level permissions in DRF.
Designed and implemented a policy evaluation engine with priorities, effects, and conditions.
Learned how to structure DRF projects with serializers, nested serializers, pagination, and permissions.
Practiced advanced database relationships (ForeignKey, related_name, select_related) for efficient queries.
Learned how to connect multiple apps cohesively for a real-world backend system.
