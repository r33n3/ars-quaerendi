# Example: Promote a temporary A2A task helper

A prototype completes one remote task correctly (O). It is **not** automatically production-ready.

Operating envelope: two authenticated agents, read-only requests, fixed tool version. This example uses optional agent-to-agent (A2A) collaboration; no particular framework or network is required.

Invariants: request IDs unique, duplicates have no extra side effects, cancellation is reconciled, peer-side permission check remains authoritative.

Fault tests: duplicate delivery, disconnect/reconnect, owner restart, malformed result, timeout after execution.

If duplicate delivery causes repeated effects, mark the promotion **revise**. Preserve the working single-run prototype and the identified failure mechanism as separate contributions. Re-test after adding idempotency and reconciliation. Judgment's recommendation is scoped; the user and host environment control authorization.
