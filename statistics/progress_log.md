# Statistics Study Progress Log

## Book: Statistics by Freedman, Pisani, Purves (4th Edition)

---

## 2026-04-04: Parts II, III, and IV Review

**Status:** In Progress
**Confidence:** 4/5

### Concepts Covered

**Chapter 3: Histograms**
• Area represents percentage, not height
• Density scale: height = percent per unit (used when intervals are unequal width)
• Equal-width histograms: height works because all bars have same width
• Variable types: discrete (countable: 0,1,2...) vs continuous (any value in range)
• Confounding variables: lurking third variable that correlates with both X and Y

**Chapter 4: Average and Standard Deviation**
• SD = root-mean-square distance from mean (typical spread)
• Why square deviations: smooth for calculus, variance adds for independent variables, penalizes outliers more
• Variance = average of squared deviations
• SD = square root of variance
• MAD (Mean Absolute Deviation) = average of absolute deviations, more robust to outliers
• Transformations:
  • Add constant: mean shifts, SD unchanged
  • Multiply by constant: both mean and SD get multiplied
• The 68-95-99.7 rule only applies to normal distributions, not a definition of SD

**Part III: Correlation and Regression**
• Correlation: symmetric, single number from -1 to +1, measures strength/direction of linear relationship
• Regression: asymmetric, gives equation y = a + bx for prediction
• Slope formula: slope = r × (SD_y / SD_x)
• r² = proportion of variance in Y explained by X
• "Variance explained" = how much better predictions are vs just guessing the mean
• Regression to the mean: extreme observations tend to be followed by less extreme ones (luck doesn't repeat)
• Named "regression" because Galton saw children's heights "regress" toward average

**Residuals**
• Residual = actual - predicted
• Good residual plot: random scatter around zero
• U-shape or curve: relationship isn't linear, need curved model
• Funnel shape: heteroscedasticity (variance not constant), try log transform
• Extrapolation: dangerous because relationship may change outside data range

**Part IV: Probability**
• Independence: P(B|A) = P(B) — knowing A doesn't change probability of B
• Dependent events: P(A and B) = P(A) × P(B|A)
• Independent events: P(A and B) = P(A) × P(B)
• Conditional probability: P(A|B) means "probability of A given B happened"
• Bayes theorem: P(A|B) = P(B|A) × P(A) / P(B)
  • Flips conditional probabilities
  • Accounts for base rates
• Base rate fallacy: ignoring how rare something is (disease testing example - 95% accurate test, 1% disease rate → only 16% chance you're sick if positive)
• Bertrand box paradox: 2/3 not 1/2, because observing gold updates probability of which box you're in

**Precision and Recall**
• Precision: of everything you flagged positive, how many were actually positive?
• Recall: of all actual positives, how many did you catch?
• Tradeoff: higher recall = more false positives (lower precision)
• Threshold slider: adjust cutoff to balance precision/recall
• Use case determines priority: cancer screening = high recall, criminal conviction = high precision

**Expected Value**
• Long-run average of a random process
• E = Σ (outcome × probability)
• Die roll: E = (1+2+3+4+5+6)/6 = 3.5
• Expected profit = expected winnings - cost
• Casinos: every game has negative expected value for player
• Recursive expected value: "expected flips to get heads" = 2 (use E inside its own definition)

### Gaps Identified
• Initially thought height represents percentage in histograms (corrected)
• Initially described SD using 68% rule without understanding it's specific to normal distribution (corrected)
• Didn't know formula connecting slope and correlation (learned)
• Didn't know what r² conceptually means (learned: variance explained)
• Bayes theorem was shaky (now solid after multiple problems)
• Didn't know range of correlation is -1 to +1 (corrected)
• Confused on Bertrand box paradox initially (now understands updating probabilities based on evidence)

### Next Up
• Expected value: recursive problems (expected rolls to get 6)
• Part V: Chance Variability (standard error, law of averages)
• Part VI: Sampling
• Parts VII-VIII: Inference (confidence intervals, hypothesis testing)

---

## Previous Sessions

### 2026-04-03: Chapter 0x250 - Getting Your Hands Dirty (Hacking book)
See: /Users/danielbrooks/learning/hacking/progress_log.md
