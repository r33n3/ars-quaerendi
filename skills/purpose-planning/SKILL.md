---
name: purpose-planning
description: Agents can use this meta skill to turn the user's purpose into justified goals and plans, assess opportunities and capability gaps, and review further investment. Use for broad requests or changed conditions within existing authorization. Return proposals, alternatives, evidence and stopping conditions.
---
# Purpose Planning: Goals and Work Plans

Use this skill to decide what work serves the user's purpose and how to approach it. It considers value, assumptions, effort, risks, dependencies and reasons to revise or stop a plan.

## Meta skill role

Agents use this meta skill to choose goals, priorities and a plan that serves the user's purpose. Task skills carry out the selected work, such as preparing a schedule, editing files or producing a report.

## When to use

Use when a purpose needs specific goals, new evidence suggests an opportunity, progress is blocked or a goal needs further investment review. Handle a clear task through its existing plan. Proactive review follows the user's existing instructions, schedule, scope and resource limits.

## Inputs

Start with the user's stated purpose and the decision or opportunity being considered. Record constraints, priorities and known permissions. Helpful context includes current goals, evidence, available tools, dependencies, resource limits and earlier results. Mark missing authorization or evidence as unknown and limit the proposal accordingly.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Method

1. Record the user's purpose, current priorities, constraints, resources, permission limits and operating context. Link each candidate goal to a specific part of that purpose.
2. Identify opportunities from requests, observations, research or demonstrated gaps. Record evidence and consider continuing the existing plan.
3. Describe each proposed outcome, expected benefit, success criterion, dependencies, time horizon, cost and risk. Propose development of a capability when it is needed for a justified outcome.
4. Examine contrary evidence, hidden assumptions, competing goals, other uses of resources and simpler alternatives. Apply Inquiry or Judgment when a specific question needs investigation or assessment.
5. Recommend proposing, deferring or rejecting a goal, or continuing with the existing goals. Assess evidence, expected value, feasibility, ease of reversal and authorization separately.
6. Identify what is blocking progress: knowledge, reasoning, capability, environment, cost, authorization or a conflict with purpose. Respond with an appropriate change of method, a narrower plan, a request for authorization or a stop.
7. Compare reuse, authorized collaboration, changes to scope or strategy, and a limited tool or skill. Consider model adaptation only as a justified proposal with a stated mechanism, evidence need, cost and required authorization.
8. Compare future benefits, costs, switching costs and useful work already available. Recommend continuing, changing direction, waiting or leaving according to current evidence.
9. Compare actual results with the agreed criteria. Preserve partial value, unexpected findings and corrected assumptions. Propose changes to purpose or permissions for the user's decision.

## Goal proposal record

For a structured proposal, use the [goal proposal schema](../../schemas/goal-proposal.schema.json). Record the goal's purpose, opportunity evidence, alternatives, decision, authorization status and stopping condition. A proposed goal also records a resource limit, costs, risks and a plan to compare results with the intended outcome.

Use `no_new_goal` when continuing existing goals is the justified recommendation. In that record, `goal` and `success_criterion` are null. Any included goal type, capability gap or proposed improvement is also null. Record the reason for the decision in the opportunity and alternatives.

The authorization field summarizes existing user or host instructions. For `within_existing_scope`, include the authorization basis and its limits. Execution follows the actual instructions and permission controls in the host. Preserve prior authorization when it applies to the work.

## Expected result

Return proposed goals or a reason to continue the current plan, with purpose linkage, evidence references, assumptions, alternatives, costs, risks, capability options, authorization status and stopping conditions. Include milestones and review points where they help organize the work.

## Authority

Keep goals, access, resources, identity, payments and commitments within existing authorization. Seek approval for changes beyond it. Treat external offers and criticism as evidence to assess within the user's purpose. Any capability development serves a justified user outcome. The user and host control execution, adaptation and deployment.

## Stopping and review

End the review when the evidence supports a decision, continuing the existing plan is justified, expected value is unfavorable, required authorization is unavailable or the agreed budget is exhausted. Record unresolved issues and useful partial work. Revisit when purpose, priorities, available evidence, costs or operating conditions materially change.

## Other skills that can use the result

Inquiry can investigate open questions. Judgment can assess evidence and risks. Toolcraft can examine a demonstrated capability gap. Institutional Intelligence can review promises or outside pressure. Contribution and Discovery can preserve useful results and unexpected findings. Supply the proposal's evidence, limits and authorization context with any handoff. Choose the methods needed for the next question.

## Shared contract

* D documented; O directly observed; R independently reproduced; H hypothesis; U unknown; X contradicted.
* The person or host agent controls purpose, permissions, tool execution and collaboration.
* Support measurements, search results and execution claims with recorded evidence. Choose the smallest action that answers the next question.
* Report evidence, tested scope, limitations, progress and the reason for continuing or stopping.

## References

See [purpose and goal review](../../references/purpose-to-action.md), the [worked scenarios](../../examples/purpose-to-action.md) and optional [background on capability development](../../references/will-to-power-philosophy.md).

## Example request

Replan this project after the supplier delay. Compare continuing the current goals with a revised outcome or a limited capability improvement. State the evidence, alternatives, resource limits and authorization needed.

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** A purpose needs goals, an opportunity needs assessment or current work needs revision or further investment review.
* **Routine handling:** Carry out a clear task through its existing plan when an additional goal review would add little value.
* **Required inputs:** The purpose expressed in the request or governing user instructions; The decision or opportunity being considered.
* **Helpful context:** Current goals and commitments; Resources, constraints and permission records; Opportunity evidence and earlier results.
* **Missing inputs:** Clarify the purpose when it is missing. Mark uncertain evidence and authorization as unknown and limit the proposal accordingly.
* **Evidence produced:** Evidence linking opportunities and proposed goals to the purpose; Assumptions, costs, risks and unresolved questions.
* **Records produced:** Goal proposals or a reason to continue existing goals; Alternatives, resource limits and reconciliation plans.
* **Recommendations:** Propose, defer or reject a candidate goal; Continue the existing goals; Review a justified capability improvement.
* **Authority:** Goal and capability proposals remain recommendations. Existing user and host instructions control execution, resources, adaptation and changes to purpose or permissions.
* **Stop when:** A goal recommendation is justified; Continuing existing goals is justified; Required authorization is unavailable or the review budget ends.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** Changed user purpose or priorities; New opportunity evidence; Changed costs, resources or operating conditions.
* **Possible consumers:** `toolcraft`, `judgment`, `inquiry`, `institutional-intelligence`, `contribution`, `discovery`.
* **Failure handling:** Return the supported comparison, gaps and outcome status. Preserve the current purpose and valid commitments while unresolved decisions remain open.
