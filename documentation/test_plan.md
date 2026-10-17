# Dominoes Test Automation: ECP/BVA Plan

Prepared: October 18, 2026. Owners: Saim and Ahmed.

Status: planned scenarios. Assignment test files, CSV files, Excel cases, and execution results have not yet been created by this plan.

## Scope and source review

Repository: https://github.com/msaimnaveed2005/dominoes-test-automation

Original project: https://github.com/abw333/dominoes

The local `dominoes/domino.py`, `dominoes/hand.py`, and `dominoes/board.py` were inspected and match the corresponding files in the local original checkout at commit `ea9f532c9b834117a5c07d214711515872f7537e` (ignoring line-ending differences).

The three developer test files were also reviewed. They contain 8, 11, and 4 test methods respectively: 23 methods in total. One method may check multiple scenarios. This is a source inspection, not a test execution or a coverage measurement.

Existing tests already cover inversion, equality, membership, hashing through set membership, basic formatting, ordinary draw/play, empty endpoints, and ordinary matching/mismatching board additions. Several planned cases intentionally provide regression coverage. Extensions include indexing/insertion boundaries, duplicate removal, dictionary/set behavior across collections, repeated failures, and recovery after an invalid move. Do not claim that all planned cases cover previously untested behavior.

## Notation and techniques

- `[a|b]` means `Domino(a, b)`. Sequences list tiles in their actual stored order.
- ECP (equivalence class partitioning) selects cases from distinct behavioral groups, such as a match, a reversed match, or no match.
- BVA (boundary value analysis) applies where a real ordered boundary exists, particularly indexing and insertion positions.
- Empty/one/multiple-item collections are useful state boundaries. Tile values 0 and 6 represent the normal double-six game domain, but the constructor does not enforce a 0-6 range. Do not expect a range-validation error.
- Orientation must be checked using `.first` and `.second` or ordered pairs. Domino equality ignores orientation, so equality alone cannot verify reversal.
- Do not assume unequal objects have different hashes: hash collisions are allowed.
- Every test starts with fresh objects. Ordered runs demonstrate configured execution order; tests must still be independent. Parallel runs do not promise a global execution sequence.

## Planned case counts

| Owner | Domino | Hand | Board | Total |
| --- | ---: | ---: | ---: | ---: |
| Saim | 20 | 25 | 15 | 60 |
| Ahmed | 25 | 20 | 15 | 60 |
| Total | 45 | 45 | 30 | 120 |

Each numbered entry below is one planned scenario, even when it requires several assertions. Numbered entries become case IDs by appending a two-digit number to the section prefix, for example `S-D-INV-01`. Parameterized collection counts must be reported separately from the number of Python test functions.

The working target is 5-10 cases for each selected method per owner. The PDF also discusses class/module totals and functions of a class; confirm the instructor's intended counting and method scope before finalizing quantities. This document does not claim to test every function in each class.

## Saim: Domino (20 cases)

### S-D-INV: `Domino.inverted()` (10 cases)

Technique: ECP for non-double/double tiles and orientation; property checks for repeated inversion.

1. `[0|6]` becomes `[6|0]`.
2. `[6|0]` becomes `[0|6]`.
3. `[2|5]` becomes `[5|2]`.
4. `[5|2]` becomes `[2|5]`.
5. `[0|0]` keeps the same values.
6. `[6|6]` keeps the same values.
7. `[3|3]` keeps the same values.
8. Invert `[2|5]` twice; its stored orientation is restored.
9. Invert `[0|6]` twice; its stored orientation is restored.
10. Invert `[2|5]`; the result is a different object and the original object's two values remain unchanged.

### S-D-EQ: `Domino.__eq__()` between Domino objects (10 cases)

Technique: ECP for identical, reversed, partially matching, and unrelated tiles.

1. `[0|0] == [0|0]` is true.
2. `[6|6] == [6|6]` is true.
3. `[2|5] == [2|5]` is true.
4. `[2|5] == [5|2]` is true.
5. `[0|6] == [6|0]` is true.
6. `[2|5] == [2|4]` is false.
7. `[2|5] == [3|5]` is false.
8. `[2|2] == [2|5]` is false.
9. `[0|0] == [6|6]` is false.
10. `[1|4] == [2|3]` is false even though the tile totals match.

## Ahmed: Domino (25 cases)

### A-D-CON: `Domino.__contains__()` (10 cases)

Technique: ECP for membership on the first side, second side, both sides, or neither.

1. `0 in [0|6]` is true.
2. `6 in [0|6]` is true.
3. `3 in [0|6]` is false.
4. `2 in [2|5]` is true.
5. `5 in [2|5]` is true.
6. `4 in [2|5]` is false.
7. `0 in [0|0]` is true.
8. `6 in [6|6]` is true.
9. `1 in [0|0]` is false.
10. `5 in [6|6]` is false.

### A-D-HASH: `Domino.__hash__()` and its equality contract (5 cases)

Technique: property checks for equal objects and collection lookup.

1. `[0|6]` and `[6|0]` have equal hashes.
2. Two separately created `[3|3]` tiles have equal hashes.
3. A set containing `[0|6]`, `[6|0]`, and `[1|1]` has two entries.
4. A dictionary keyed by `[2|5]` can be read using `[5|2]`.
5. Updating that dictionary through `[5|2]` updates the same entry and keeps its length at one.

### A-D-STR: `Domino.__str__()` (5 cases)

Technique: ECP for doubles/non-doubles and different orientations. Expected strings are exact.

1. `[0|0]` produces `"[0|0]"`.
2. `[0|6]` produces `"[0|6]"`.
3. `[6|0]` produces `"[6|0]"`.
4. `[6|6]` produces `"[6|6]"`.
5. `[2|5]` produces `"[2|5]"`.

### A-D-EQ: `Domino.__eq__()` with other object types (5 cases)

Technique: ECP by object type. Compare with a `[2|5]` tile on the left.

1. Compare with `None`: false.
2. Compare with integer `2`: false.
3. Compare with tuple `(2, 5)`: false.
4. Compare with list `[2, 5]`: false.
5. Compare with a separate namedtuple type exposing `first=2` and `second=5`: false.

## Saim: Hand (25 cases)

### S-H-DRAW: `Hand.draw()` (10 cases)

Technique: ECP plus BVA around insertion positions. Let `A=[0|1]`, `B=[2|3]`, and new tile `X=[5|6]`. Unless stated otherwise, the initial hand is `[A, B]`. Each draw returns `None` and adds one tile.

1. Empty hand, default index: `[X]`.
2. One-tile hand `[A]`, default index: `[A, X]`.
3. Two-tile hand, default index: `[A, B, X]`.
4. Index `0`: `[X, A, B]`.
5. Index `1`: `[A, X, B]`.
6. Index `2` (equal to length): `[A, B, X]`.
7. Index `3` (one beyond length): `[A, B, X]`; list insertion clamps to the end.
8. Index `-1`: `[A, X, B]`.
9. Index `-2`: `[X, A, B]`.
10. Index `-3` (below the negative length boundary): `[X, A, B]`.

### S-H-GET: `Hand.__getitem__()` (10 cases)

Technique: BVA. Initial hand is `[A, B]` unless stated otherwise. Compare stored orientations when checking results.

1. Index `0`: returns A.
2. Index `1`: returns B.
3. Index `2`: raises `IndexError`.
4. Index `-1`: returns B.
5. Index `-2`: returns A.
6. Index `-3`: raises `IndexError`.
7. Empty hand, index `0`: raises `IndexError`.
8. Empty hand, index `-1`: raises `IndexError`.
9. One-tile hand `[A]`, index `0`: returns A.
10. One-tile hand `[A]`, index `1`: raises `IndexError`.

### S-H-LEN: `Hand.__len__()` (5 cases)

Technique: ECP/state boundaries for collection size.

1. Empty hand: length 0.
2. One-tile hand: length 1.
3. Two-tile hand: length 2.
4. Hand containing duplicate tiles `[A, A]`: length 2; duplicates are counted.
5. Seven-tile hand: length 7; this is a representative initial game hand, not an enforced maximum.

## Ahmed: Hand (20 cases)

### A-H-PLAY: `Hand.play()` (10 cases)

Technique: ECP for present/reversed/duplicate/missing tiles, with empty and singleton boundaries. Let `A=[0|1]`, `B=[2|3]`, `C=[4|5]`, and missing tile `X=[6|6]`.

1. Play A from `[A]`: returns index 0 and leaves an empty hand.
2. Play A from `[A,B,C]`: returns 0 and leaves `[B,C]`.
3. Play B from `[A,B,C]`: returns 1 and leaves `[A,C]`.
4. Play C from `[A,B,C]`: returns 2 and leaves `[A,B]`.
5. Play `[1|0]` from `[A,B]`: returns 0 and leaves `[B]`.
6. Play A from `[A,A,B]`: returns 0 and leaves `[A,B]`; only one duplicate is removed.
7. Play A from `[B,A,A]`: returns 1 and leaves `[B,A]`; the first equal tile is removed.
8. Play X from `[A,B]`: raises `NoSuchDominoException`; stored contents and order are unchanged.
9. Play X from an empty hand: raises `NoSuchDominoException`; the hand stays empty.
10. Play A from `[A]`, then try to play A again: the first removal succeeds, the second raises `NoSuchDominoException`, and the hand remains empty.

### A-H-FIND: `hand.contains_value()` (10 cases)

Technique: ECP for empty, present at different positions, repeated, and absent values.

1. Empty hand, search 0: false.
2. Hand `[[0|6]]`, search 0: true.
3. Hand `[[0|6]]`, search 6: true.
4. Hand `[[0|6]]`, search 3: false.
5. Hand `[[3|3]]`, search 3: true.
6. Hand `[[0|1],[2|3]]`, search 3: true.
7. Hand `[[0|1],[2|3]]`, search 6: false.
8. Hand `[[0|0],[6|6]]`, search 0: true.
9. Hand `[[1|2],[2|3],[3|4]]`, search 2: true even though it occurs in multiple tiles.
10. Hand `[[0|1],[2|3],[4|6]]`, search 6: true at the last tile.

Also assert that searches leave the hand contents and order unchanged.

## Saim: Board (15 cases)

### S-B-ADD: `Board.add(tile, left=True)` (10 cases)

Technique: ECP for an empty board, a direct match, a reversed match, a double, or a mismatch. Each case uses fresh objects.

1. Empty board + `[0|6]`: result `[0|6]`, length 1.
2. Empty board + `[6|6]`: result `[6|6]`, length 1.
3. Board `[2|5]` + `[3|2]`: result `[3|2][2|5]`.
4. Board `[2|5]` + `[2|3]`: result `[3|2][2|5]`; the added tile is reversed.
5. Board `[2|5]` + `[2|2]`: result `[2|2][2|5]`.
6. Board `[0|6]` + `[3|0]`: result `[3|0][0|6]`.
7. Board `[2|5]` + `[1|4]`: raises `EndsMismatchException`; length, endpoints, and stored tile orientations are unchanged.
8. Board `[2|5]` + `[4|4]`: raises `EndsMismatchException`; board is unchanged.
9. From `[2|5]`, add `[3|2]`, then `[4|3]`: result `[4|3][3|2][2|5]`, left endpoint 4, right endpoint 5, length 3.
10. From `[2|5]`, reject `[1|4]`, then add `[3|2]`: result `[3|2][2|5]`; failure does not prevent a later valid move.

In successful additions, assert that the opposite endpoint remains unchanged when the board was already nonempty.

### S-B-END: `Board.left_end()` (5 cases)

Technique: ECP/state boundaries for empty, singleton, and extended boards.

1. Empty board: raises `EmptyBoardException`.
2. Board `[0|6]`: returns 0.
3. Board `[6|0]`: returns 6.
4. Board `[3|3]`: returns 3.
5. Board built by starting with `[2|5]` and adding `[3|2]` on the left: returns 3 and leaves the board unchanged.

## Ahmed: Board (15 cases)

### A-B-ADD: `Board.add(tile, left=False)` (10 cases)

Technique: ECP for an empty board, a direct match, a reversed match, a double, or a mismatch. Each case uses fresh objects.

1. Empty board + `[6|0]`: result `[6|0]`, length 1.
2. Empty board + `[0|0]`: result `[0|0]`, length 1.
3. Board `[2|5]` + `[5|3]`: result `[2|5][5|3]`.
4. Board `[2|5]` + `[3|5]`: result `[2|5][5|3]`; the added tile is reversed.
5. Board `[2|5]` + `[5|5]`: result `[2|5][5|5]`.
6. Board `[6|0]` + `[0|3]`: result `[6|0][0|3]`.
7. Board `[2|5]` + `[1|4]`: raises `EndsMismatchException`; length, endpoints, and stored tile orientations are unchanged.
8. Board `[2|5]` + `[4|4]`: raises `EndsMismatchException`; board is unchanged.
9. From `[2|5]`, add `[5|3]`, then `[3|4]`: result `[2|5][5|3][3|4]`, left endpoint 2, right endpoint 4, length 3.
10. From `[2|5]`, reject `[1|4]`, then add `[5|3]`: result `[2|5][5|3]`; failure does not prevent a later valid move.

In successful additions, assert that the opposite endpoint remains unchanged when the board was already nonempty.

### A-B-END: `Board.right_end()` (5 cases)

Technique: ECP/state boundaries for empty, singleton, and extended boards.

1. Empty board: raises `EmptyBoardException`.
2. Board `[6|0]`: returns 0.
3. Board `[0|6]`: returns 6.
4. Board `[3|3]`: returns 3.
5. Board built by starting with `[2|5]` and adding `[5|3]` on the right: returns 3 and leaves the board unchanged.

## Implementation and traceability

1. Implement these cases in the six member-specific test files listed in `task_allocation.md`.
2. Use stable case IDs as parameter IDs. A Python test function can execute multiple cases through parameterization.
3. For a simple CSV starting point, Saim can externalize `S-D-INV-01` through `S-D-INV-04`; Ahmed can externalize `A-D-CON-01` through `A-D-CON-04`. These rows are part of the planned totals, not additional cases. CSV values must be converted to the correct Python types.
4. CSV schemas can be `case_id,first,second,expected_first,expected_second` for inversion and `case_id,first,second,search_value,expected_contains` for membership. Parse boolean values explicitly; `bool("False")` is true and is not a correct CSV boolean conversion.
5. Use member markers (`saim`, `ahmed`), module markers (`domino`, `hand`, `board`), and a CSV marker where applicable. Register all custom markers.
6. Document separate commands for the full assignment suite, each member, each module, CSV cases, parallel execution, and ordered execution. Do not promise sequential global order in a parallel run.
7. Excel columns should include case ID, owner, module/method, technique, preconditions, steps, input, expected result, actual result, status, and automated test reference. Use `Not run` until a real execution occurs.
8. Keep implementation, documentation, and actual collected case counts consistent. Record the interpreter, dependency versions, commands, and results after execution.

The plan itself has been checked for consistent numbering and balanced allocation. Its scenarios still require implementation and execution; no pass/fail results are claimed here.
