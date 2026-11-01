# Purpose and goal review

Use this method when an authorized purpose needs specific goals, new evidence suggests an opportunity, progress is blocked or further investment needs review. Proactive activity follows the user's existing instructions, schedule, scope and resource limits. The host manages any scheduling and execution.

## Objects to record

* Purpose: the user's stated reason for the work. Preserve its wording and record changes authorized by the user.
* Opportunity: a reported, observed or hypothesized contribution worth considering.
* Goal: a desired outcome linked to the purpose, with a success criterion and limits.
* Capability gap: a missing ability that prevents a justified goal from being reached.
* Improvement: a proposed use of existing resources, collaboration, a changed plan, a tool or a justified adaptation mechanism.
* Evidence: source records and observations with their scope and uncertainty.

Assess value, evidence maturity and authorization separately. A proposed goal is a recommendation for consideration. Execution follows the user's actual instructions and host controls.

## Conditions affecting a plan

| Condition | Useful response |
|---|---|
| Missing knowledge | Investigate a question that could change the decision. |
| Uncertain reasoning | Compare explanations or use a simpler approach. |
| Missing capability | Compare reuse, authorized collaboration, adaptation and a limited helper. |
| Unsuitable environment | Narrow the scope, change the plan or defer. |
| Excessive cost | Compare expected benefits, future costs and alternatives. |
| Missing authorization | Seek approval when useful or stop the proposed action. |
| Conflict with purpose | Reject or reformulate the goal. |

## Proposal format

Use the [goal proposal schema](../schemas/goal-proposal.schema.json) when a structured record helps organize the decision. Record the purpose, opportunity, goal, success criterion, evidence status, evidence references, alternatives, authorization status, recommendation and stopping condition.

The evidence status applies to the opportunity evidence. Cite supporting records when classifying it as documented, observed, reproduced or contradicted. A hypothetical scenario or proposed test uses an appropriate hypothesis or unknown status.

For a proposed goal, also record a resource limit, costs including effects on other work, risk and ease of reversal, and a plan to compare actual results with the intended outcome. A developmental goal records the capability gap and proposed improvement. State the actual adaptation mechanism and authorization needed when model changes are proposed.

For `no_new_goal`, `goal` and `success_criterion` are null. Any included goal type, capability gap or proposed improvement is also null. Explain why continuing current goals is justified through the opportunity, alternatives and review conditions.

For `within_existing_scope`, record the authorization basis, such as the applicable user instruction and its scope or resource limits. The field summarizes an existing record. Execution still follows the actual instructions and available permission controls. Preserve authorization already granted for the work. Use `unknown` when a basis is unavailable. A prohibited goal can be rejected or the review can end with the current goals unchanged.

See the [worked scenarios](../examples/purpose-to-action.md), [goal proposal](../examples/purpose-to-action-goal.json) and [current goals example](../examples/purpose-to-action-no-goal.json).

## Further investment

Compare the next use of time, money or computing resources with the available alternatives. Evaluate future benefits, future costs, switching costs and useful work already available. Record past spending separately. Research value, user value and financial value may need different evidence and measures. Preserve useful methods and findings when work ends.

## Review effort and stopping

Choose the smallest evidence request that could change the decision. Start with one focused challenge and a limited revision when review is useful. Expand for concrete consequential risks or a user request.

Stop when the evidence supports the recommendation, the budget is exhausted, required authorization is unavailable or expected value is unfavorable. Record the reason and remaining uncertainty. Reopen the review when priorities, costs, evidence, resources or operating conditions materially change.

## Skills that can use the record

Inquiry can investigate a stated uncertainty. Judgment can assess the evidence and risk. Toolcraft can propose a way to supply a capability. Institutional Intelligence can examine promises, incentives or pressure affecting the goal. Contribution and Discovery can retain useful partial results, reusable methods and new leads.

Send the relevant purpose, proposal, evidence references, limitations and authorization context with each handoff. Apply the methods needed for the next question.
