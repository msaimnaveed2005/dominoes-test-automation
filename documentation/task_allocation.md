# Dominoes Test Automation: Task Allocation

Prepared: October 18, 2026. Status: proposed allocation; implementation and results are pending.

Group repository: https://github.com/msaimnaveed2005/dominoes-test-automation

Original project: https://github.com/abw333/dominoes (Alan Wagner, MIT license).

## Members and responsibilities

| Work | Saim | Ahmed |
| --- | --- | --- |
| Domino module | `inverted()` and equality between Domino objects | Membership, hashing, string formatting, comparison with other object types |
| Hand module | `draw()`, indexing, and hand size | `play()` and `hand.contains_value()` |
| Board module | Left-side additions and `left_end()` | Right-side additions and `right_end()` |
| ECP/BVA documentation | Explain the input groups and applicable boundaries for Saim's cases | Explain the input groups and applicable boundaries for Ahmed's cases |
| External test data | CSV data and parameterized tests for Saim's cases, including at least four CSV rows | CSV data and parameterized tests for Ahmed's cases, including at least four CSV rows |
| Excel documentation | Document Saim's case IDs, inputs, expected results, and actual results after execution | Document Ahmed's case IDs, inputs, expected results, and actual results after execution |
| Configuration | Test markers, module/member suites, and ordered execution demonstration | Parallel execution configuration and CSV parameterization support |
| Setup and video | Verify repository setup and record the setup demonstration | Independently follow the setup instructions and document reproducible installation |
| Summary report | Report Saim's work and results | Report Ahmed's work and results |
| Final verification | Review Ahmed's instructions and test design | Review Saim's instructions and test design |

## Files

Saim:

- `assignment_tests/test_domino_saim.py`
- `assignment_tests/test_hand_saim.py`
- `assignment_tests/test_board_saim.py`
- `test_data/saim_cases.csv`

Ahmed:

- `assignment_tests/test_domino_ahmed.py`
- `assignment_tests/test_hand_ahmed.py`
- `assignment_tests/test_board_ahmed.py`
- `test_data/ahmed_cases.csv`

Shared documentation:

- `documentation/task_allocation.md`
- `documentation/test_plan.md`
- `documentation/test_cases.xlsx`, with separate Saim and Ahmed sheets
- Setup instructions, configuration documentation, setup video, and summary report

Agree on one editor for shared configuration files at a time. Each member should review and be able to explain every configuration feature during evaluation.

## Planned quantities

The accompanying plan proposes 60 scenarios for Saim and 60 for Ahmed. Each selected method has 5-10 scenarios per owner. `Board.add()` is divided by its left/right input, and `Domino.__eq__()` is divided by comparison type.

These are planning targets, not completed-test counts. The assignment uses overlapping wording about counts per function and per class/module. Confirm how the instructor counts selected methods, parameterized cases, and class/module totals before treating this plan as final compliance. The selected-method scope does not include every method in each class.

Four CSV rows per member is our proposed allocation; the PDF states at least four without clearly saying that this number applies to each person.

## Contribution evidence

1. Preserve the developer's original `tests/` and license.
2. Keep new assignment tests in `assignment_tests/`.
3. Each member reviews and commits their own work using their own Git identity.
4. Record actual execution results only after running the tests.
5. Describe overlap with developer tests honestly. Different input numbers alone do not establish a new test objective.
6. Do not create commits under another member's identity or claim completed work before it exists.

The summary report should link case IDs and commits to the responsible member.
