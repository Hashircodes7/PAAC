# Policy-Aware Access Control (PAAC) Project

## Overview
The Policy-Aware Access Control (PAAC) project is a Django-based system designed to enforce fine-grained access control using policies, roles, and conditions. This project has been developed as a learning journey to strengthen my backend skills, explore Django REST Framework, and implement robust access control logic with multiple interconnected apps.

## Key Highlights:
Built multiple Django apps for modularity: identity_app, policy_engine, decision_engine, audit_log, and simulation_mode.
Implemented JWT-based authentication with role-based permissions.
Learned advanced DRF concepts such as custom serializers, pagination, nested serializers, and object-level permissions.
Developed a dynamic policy evaluation engine that matches user attributes with policy conditions.
Integrated audit logging and simulation functionality to analyze access control decisions.
Applied real-world design patterns to connect multiple apps cohesively.

## Features

### Identity App
- Custom User model with roles: `ceo`, `manager`, `employee`, `intern`, `auditor`.
- Departments for users.
- Full CRUD operations for users.
- Role-based permissions for access control.
- Pagination for listing users.

### Policy Engine
- CRUD operations for policies with attributes: priority, effect (allow/deny), action, and resource type.
- JSON-based conditions to define applicable users.
- Server-side validation for policy attributes.
- Role-based access:
  - CEO can manage policies.
  - Managers and auditors can view policies.

### Decision Engine
- Evaluates access requests based on user attributes and policies.
- Stores decisions in the database with reasons.
- Nested serializers include full user and policy information.
- Pagination for listing decisions.

### Audit Log
- Tracks all decisions with timestamps.
- Filters audits by user or policy.
- Access restricted to auditors and CEO.

### Simulation Mode
- Simulates access decisions for users before applying policies.
- Prevents self-simulation.
- Supports role-based access to simulations.
- Integrated with the decision evaluation engine.

## Learning Outcomes
- Built and integrated five distinct apps with complex relationships.
- Applied role-based and object-level permissions in DRF.
- Designed and implemented a policy evaluation engine with priorities, effects, and conditions.
- Learned DRF project structuring with serializers, nested serializers, pagination, and permissions.
- Practiced advanced database relationships (ForeignKey, related_name, select_related) for efficient queries.
- Learned how to connect multiple apps cohesively for a real-world backend system.
