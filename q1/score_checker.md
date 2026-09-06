# PSHS Student Score Checker

**Name:** [James Matthew A. Mariño]  
**Section:** [8-Dahlia]  

## Activity Overview
In this activity, I improved a Student Score Checker program by applying proper coding.
The program accepts a student score from 0 to 100 and shows the classification.

The classifications are:
| Score | Classification |
|---|---|
| 90-100 | Outstanding |
| 80-89 | Very Satisfactory |
| 75-79 | Satisfactory |
| 0-74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.

---

# Part 1 - Analyze the Logic

## Input
**What information does the program need?**
> The program needs an integer value representing the student's score.

## Valid Range
* **Minimum valid score:** 0
* **Maximum valid score:** 100

## Possible Outputs
1. `Invalid Score.`
2. `Outstanding`
3. `Very Satisfactory`
4. `Satisfactory`
5. `Needs Improvement`

## Boundary Condition
**What condition will you use to determine whether the score is valid?**
> `student_score < 0 or student_score > 100` (or `0 <= student_score <= 100`).

## Multiple Decision Paths
**Explain how the program decides which classification should be displayed.**
> The program first makes sure if the score is within range. If valid, it checks the conditions top-down: checking if the score is $\ge 90$ for "Outstanding", then $\ge 80$ for "Very Satisfactory", $\ge 75$ for "Satisfactory", and defaults to "Needs Improvement" for anything below 75.

---

# Part 2 - Flowchart

```text
       [ START ]
           |
   ( Input score )
           |
    / Is score < 0  \
  <   OR score > 100? > --- YES ---> [ Display "Invalid Score." ]
    \               /                      |
           | NO                            |
    / Is score >= 90? \                    |
  <                     > --- YES --> [ Display "Outstanding" ]
    \                 /                    |
           | NO                            |
    / Is score >= 80? \                    |
  <                     > --- YES --> [ Display "Very Satisfactory" ]
    \                 /                    |
           | NO                            |
    / Is score >= 75? \                    |
  <                     > --- YES --> [ Display "Satisfactory" ]
    \                 /                    |
           | NO                            |
  [ Display "Needs Improvement" ]          |
           |                               |
           +-------------------------------+
           |
        [ END ]
```

---

# Part 3 - Pseudocode

```text
START
    INPUT score
    IF score < 0 OR score > 100 THEN
        DISPLAY "Invalid Score."
    ELSE IF score >= 90 THEN
        DISPLAY "Outstanding"
    ELSE IF score >= 80 THEN
        DISPLAY "Very Satisfactory"
    ELSE IF score >= 75 THEN
        DISPLAY "Satisfactory"
    ELSE
        DISPLAY "Needs Improvement"
    END IF
END
```

---

# Part 4 - Clean Code Implementation

Refer to `score_checker.py` in the same directory for source code.

---

# Part 5 - Testing

| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---|---|---|---|---|
| 1 | -1 | Below minimum | Invalid Score. | Invalid Score. | PASS |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | PASS |
| 3 | 74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | PASS |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | PASS |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS |
| 8 | 101 | Above maximum | Invalid Score. | Invalid Score. | PASS |

## Testing Reflection

### 1. Why is it important to test the values 0 and 100?
> They represent the exact minimum and maximum boundaries. Testing them ensures the program correctly includes values as valid.

### 2. Why did you also test -1 and 101?
> They are off by one values directly outside the valid range. Testing them verifies that the invalid range boundary works properly.

### 3. Which test helped you understand boundary conditions the most?
> Testing inputs like 74 and 75, as well as 100 and 101, showed exactly where the numbers might give a different result such as an another classification or invalid score.

### 4. Did any of your tests initially fail? If yes, what did you change in your program?
> No, because the checking was placed before evaluation of students grades.

---

# Reflection

### 1. How did selection structures make the program more useful?
> Selection structures allows the program to do different actions based on what the user puts, it enables validation and classification.

### 2. How did proper comments and readable formatting improve your program?
> Descriptive variable names and standard indentation make the code easier to read and understand for other developers.

### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
> Planning maps out logic flow and helps identify cases or errors early before writing the specific syntax code.
>
