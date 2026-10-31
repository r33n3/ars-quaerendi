# Example: Promote a temporary A2A task helper

A prototype completes one remote task correctly (O). Record this as one observed success within the tested scope. Assess deployment readiness through the tests below.

Operating envelope: two authenticated agents, read-only requests, fixed tool version. This example uses agent-to-agent (A2A) collaboration between independently authorized participants.

Invariants: request IDs are unique, duplicate delivery has the same effects as a single request, cancellation is reconciled, and each participant enforces its own permissions.

Fault tests: duplicate delivery, disconnect/reconnect, owner restart, malformed result, timeout after execution.

If duplicate delivery causes repeated effects, mark the promotion **revise**. Preserve the working single-run prototype and the identified failure mechanism as separate contributions. Re-test after adding idempotency and reconciliation. Judgment's recommendation is scoped; the user and host environment control authorization.
