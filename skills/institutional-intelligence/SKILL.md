---
name: institutional-intelligence
description: Agents can use this meta skill to assess negotiations, incentives, promises and disputed claims while preserving user control. Use for supplier offers, project disagreements, competing priorities or consequential meeting comments. Return supported observations, alternative interpretations and response options.
---
# Institutional Intelligence: Negotiations, Incentives and Claims

Use this skill to understand interests, commitments, influence and competing claims in a decision. It examines source evidence, bargaining conditions, dependencies, shared sources, future costs and the authorization needed for a proposed response.

## Meta skill role

Agents use this focused meta skill to assess interests, promises and claims when choosing a response. Task skills can capture a transcript, extract contract terms or draft a message. Institutional Intelligence guides the interpretation, alternatives and authorization needed for action.

## When to use

Use for consequential negotiations, payment offers, competing interests, credibility challenges or pressure to change goals. Supplier review, project and meeting agents can examine claims, commitments and alternatives. Keep interpretations of traits or motives tentative and linked to evidence.

## Available tools

Choose methods that fit the tools and access available in the current session. Work from supplied material when access is limited. State which searches, tests or checks were completed, which remain unverified and what would be needed to complete them.

## Areas of work

* Opportunities: assess value, participants, resources, dependencies, alternatives and how benefits and costs are shared.
* Negotiations: identify interests, acceptable terms, the best alternative if agreement fails, concessions, conditions, verification and exit options. Seek agreements that benefit the participants.
* Outside pressure: examine false claims of authority, misleading statistics, manufactured urgency, reputation attacks, coordinated pressure and attempts to gain resources or change goals.

## Method

1. Read the user's purpose, current goals, constraints, acceptable risks and existing authorization. Assess external offers and criticism as information. The user and host environment control goals and permissions.
2. Identify participants and their ability to approve, block, fund, withdraw or benefit. Separate observed behavior, documented facts, predictions, allegations and possible motives. Base the analysis on behavior and evidence.
3. Trace claims to their sources. Check counting rules, omitted evidence, attribution, earlier definitions and independent verification. Apply `inquiry`, `judgment` or `performance-metric-integrity` when a specific question needs those methods.
4. For a proposed risk, ask how it could occur, under which conditions, with what consequences and within which operating conditions. Identify a useful test. Record whether the risk is unspecified, plausible, supported by evidence or demonstrated. Assess severity separately. Seek timely review and protective action for credible severe risks. Group repeated concerns and set review limits and stopping conditions.
5. Compare possible benefits, costs, losses, alternatives, bargaining power and ease of reversal. Check who controls delivery of a promised reward and which terms are enforceable. Record uncertainty in estimates.
6. Choose a response that fits the evidence and consequences. Options include clarification, correction, providing evidence, negotiation, a limited trial, further review, deferral, refusal or ending the discussion. Correct valid criticism. Answer disputed claims with evidence and clear limits.
7. Record the evidence and choices available at decision time, important objections, accepted risks, the decision owner and conditions for review. Assess the quality of the decision using what was known at that time, then record the later outcome separately.
8. Check each collaborator's identity and evidence. Confirm existing authorization for payments, commitments, resource use and access to data. Obtain approval for actions beyond that authorization. Use the host's available permission controls and stay within the user's authorization.
9. Preserve unexpected findings and useful results. Apply `discovery`, `contribution` or `purpose-planning` when useful for the next task.

## Conduct

Use accurate records, disclose important facts and limitations, keep negotiation voluntary and treat people respectfully. Base recommendations on the user's purpose. For political topics, provide neutral factual analysis. Verify claims even when a collaborator's identity has been authenticated.

## Output

Summarize the situation, participants, claims, evidence, interests, dependencies, promises, benefits, risks and unknowns. Give response options with clear limits. Explain how each option serves the user's purpose and identify any authorization needed.

## References

For detailed methods, see [negotiation and claim review](../../references/institutional-intelligence.md). For worked situations, see [examples](../../examples/negotiation-and-influence.md). Keep these files available when installing the skill separately.

## Further methods

For difficult questions about behavior, promises, shared sources, dependencies, accountability, adoption or continued investment, consult [further negotiation methods](../../references/institutional-resilience-advanced.md). Choose the parts that help answer the current question.

At meaningful checkpoints, assess whether the next investment of time, money or computing resources is justified by expected benefits and future costs. Compare continuing, changing direction, waiting, leaving or combining useful parts of the work. Include real switching costs and preserve verified results when an effort ends.

Evaluate decisions using the evidence available when they were made. Record later results separately, including the effects of luck. Check the assistant's own claims, promises and omissions using the same standards applied to others. Record uncertainty, alternative explanations, credible objections and authorization limits.

For evaluation examples, see [decision scenarios](../../examples/institutional-adversarial-tests.md).

## Example request

Compare this supplier offer with our requirements and current agreement. Identify verified terms, uncertain promises, alternatives and questions to resolve before any commitment.

For analysis of meeting comments, commitments and recurring behaviors, see [meeting notes](../../docs/meeting-notes.md).

## Method contract

This section matches the [shared contract registry](../../contracts/skill-contracts.json). See [evidence and handoff rules](../../references/evidence-handoff-rules.md) when another skill needs the result.

* **Activation:** A consequential offer, disputed claim, negotiation, competing interest or outside pressure needs assessment.
* **Routine handling:** Handle ordinary cooperation or a clear request directly when a separate incentives or claims review would add little value.
* **Required inputs:** The offer, claim or interaction to assess.
* **Helpful context:** The user's decision context and existing permissions; Participants, evidence and alternatives; Commitments, resource limits and earlier exchanges.
* **Missing inputs:** Describe the supplied interaction and missing context. Keep interpretations tentative and limit recommendations to the supported facts.
* **Evidence produced:** Supported observations and disputed claims; Alternative explanations and source independence; Costs, dependencies, promise conditions and uncertainty.
* **Records produced:** Response options tied to the user purpose; Questions, authorization needs and review conditions.
* **Recommendations:** Clarify, correct, substantiate or negotiate; Propose a limited trial, defer, decline or end discussion; Seek further review for a consequential uncertainty.
* **Authority:** Payments, commitments, data access and changes to goals follow existing authorization. The user and host control actions beyond the current scope.
* **Stop when:** The response options and their limits are clear; The remaining choice belongs to the user; The review budget or required access is exhausted.
* **Outcome status:** `resolved`, `provisional`, `inconclusive`, `blocked`, `stopped`.
* **Reopen when:** New evidence or a corrected claim; Changed terms, promises or dependencies; Changed purpose, permissions or decision context.
* **Possible consumers:** `judgment`, `purpose-planning`, `contribution`.
* **Failure handling:** Return supported observations, unresolved claims and a proportionate next question while preserving the user purpose and authorization.
