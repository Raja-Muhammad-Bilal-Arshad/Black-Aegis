---
name: api-logic-abuse
description: BOLA, Mass Assignment, GraphQL injection.
---

# API Logic Abuse Protocol

## 1. Principles
- **APIs leak schema**: GraphQL introspection queries tell you everything.
- **IDs are predictable**: Auto-incrementing IDs allow for enumeration.
- **Objects are open**: Mass Assignment allows you to set `isAdmin: true`.

## 2. Techniques
- **BOLA (Broken Object Level Authorization)**: Changing `user_id=123` to `user_id=124`.
- **Mass Assignment**: Sending `{ "user": "test", "role": "admin" }` when the server only expects user.
- **GraphQL Injection**: Nested queries to DoS the server or extract hidden fields.

## 3. Checklist
- [ ] Swagger/OpenAPI spec found?
- [ ] BOLA testing script running?
- [ ] Hidden parameters fuzzing (Arjun)?
- [ ] Rate limits tested?
