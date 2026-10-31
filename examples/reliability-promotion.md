# Example: Prepare a shared task helper for reuse

A prototype completes one remote task correctly (O). Record this as one observed success within the tested scope. Assess deployment readiness through the tests below.

Operating conditions: two authenticated agents, requests that only read data, fixed tool version. Each agent has its own authorization.

Required conditions: request IDs are unique, duplicate delivery has the same effects as a single request, cancellation is reconciled, and each participant enforces its own permissions.

Fault tests: duplicate delivery, disconnect/reconnect, owner restart, malformed result, timeout after execution.

If duplicate delivery causes repeated effects, mark the promotion **revise**. Preserve the prototype that worked once and the identified failure mechanism as separate contributions. Test again after adding idempotency and reconciliation. Judgment's recommendation is scoped; the user and host environment control authorization.
