# Hash Code 2018 Score Calculator

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c7b68e6d417b43c48d66f76b6d02dc7f)](https://app.codacy.com/app/PicoJr/2018-hashcode-score?utm_source=github.com&utm_medium=referral&utm_content=PicoJr/2018-hashcode-score&utm_campaign=Badge_Grade_Dashboard)

**TL;DR** Compute score for Hash Code 2018 Qualification Round.

## Usage

`python3 score.py res/a_example.in res/a_example.out`

```
score: 10
```

`python3 score.py res/b_should_be_easy.in res/b_should_be_easy.out --score`

```
score: 176,877 = 169,677 + 7,200 (bonus)
```

`python3 score.py res/e_high_bonus.in res/e_high_bonus.out --score --rides --wait `

```
score: 21,465,945 = 11,588,945 + 9,877,000 (bonus)
wait time: 2,032,526
rides: 10,000 = 9,984 (taken) + 16 (unassigned) 0 (late)
rides: 9,984 (taken) = 9,877 (bonus) + 107 (no bonus)
```

## Output File Checks

The following checks are performed on the output file when the `--check` option is set

check
- [x] ride ids are correct
- [x] rides are assigned only once
- [x] number of cars
- [x] number of steps in the simulation

### Example

`python3 score.py res/b_should_be_easy.in res/b_should_be_easy.out --check`

```
INFO:root:checking vehicles
INFO:root:vehicles: OK
INFO:root:checking ride ids
INFO:root:ride ids: OK
score: 176,877
```

## Unit Tests

see `test_score.py`

## Our Team & Qualification Round

<https://hashcode.withgoogle.com/hashcode_2018.html>

Team: MetaModHell

Members (listed alphabetically): Karbok, PicoJr

Score: 46,048,775

Rank: 628th World, 81st France

### Submissions

| Input            |  Score     |
|:-----------------|-----------:|
| A-example        | 10         |
| B-should be easy | 176,877    |
| C-no hurry       | 13,052,303 |
| D-metropolis     | 11,353,640 |
| E-high bonus     | 21,465,945 |
