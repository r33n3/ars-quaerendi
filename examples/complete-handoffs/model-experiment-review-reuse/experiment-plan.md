# Proposed experiment X101

* Identifier: `X-101`.
* Status: proposed.
* Record kind: illustrative.
* Intended domain: software.
* Input evidence: `E-101`, concerning claim `C-101`.
* Candidate models: numerical rounding, tokenizer settings, runtime behavior and measurement error.
* Prediction: an effect attributable to rounding should persist when other relevant conditions are matched. A settings effect should track the changed settings in a separate comparison. Interactions may require additional tests.
* Design: use matched runtime, tokenizer, prompt, sampling settings and hardware. Include an unchanged artifact as a negative control and vary one factor at a time initially.
* Measurement checks: preserve token identifiers, numerical outputs, settings, versions and raw logs. Check repeated baseline behavior and detection sensitivity. Record any later design revisions.
* Authorization: planning only within the supplied example. Actual execution requires the user's and host's applicable permissions.
* Resource limit: one design review. Runtime and cost budgets remain to be agreed before execution.
* Result evidence: none. Execution remains unperformed.
* Stopping: stop planning when a discriminating design is recorded or a needed condition is unavailable. Record unresolved interactions and infeasible comparisons.

This plan is a related artifact. Observed results would need their own evidence records and identifiers. A test that cannot distinguish the candidate models leaves the causal question underdetermined.
