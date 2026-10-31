# Evaluator notes for the file comparison challenge

These notes describe preparation and expected evidence. Keep them separate from the investigator's task material. Record any prior exposure to this preparation when reporting the evaluation.

## Preparation

Create an original data container and a variant that changes only metadata. Verify independently that each named array has matching type, dimensions and value bytes in both files. Save the validation records as the answer key.

An optional variant adds a distinctive byte sequence outside the parsed metadata. Use it to check whether the investigator distinguishes a raw byte match from a match inside a specific field. Record where the sequence was placed.

Provide a format description and a suitable reader when available. State time, resource and access limits. If a needed instrument is unavailable, evaluate the proposed investigation and its stated limits separately from execution.

## Expected evidence

The investigator should distinguish the identity of a complete file from the identity of its components. Look for comparisons by array name, type, dimensions and value content, with coverage and decoding limits stated explicitly.

Changed metadata can move stored components to different offsets while preserving their values. Compare parsed components and check that any value hashes cover consistent representations. Different complete file hashes establish a byte difference somewhere in the file; identifying changed values requires component evidence.

For the optional byte sequence, check whether the report identifies the sequence's actual location. A claim about a metadata field needs evidence from that parsed field.

## Scoring

Record evidence accuracy, reproduction quality, instrument controls, uncertainty, resource use and response to feedback separately. Credit conclusions supported by completed checks and useful corrections of failed hypotheses. Mark uncovered parts as unresolved.

For transfer, supply a different container with a comparable distinction between file structure and named content. Record whether the investigator recognizes the connection and verifies its usefulness. Report actual runs and limits. This document describes a proposed evaluation; its effectiveness depends on measured results.
