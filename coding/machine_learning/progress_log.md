# Hands-On Machine Learning Progress Log

## 2026-04-03: Chapter 1 - The Machine Learning Landscape

**Status:** Completed
**Confidence:** 4/5

### Key Concepts Covered

**What is ML & Why Use It**
- ML learns from data instead of explicit rules
- Use when rules change over time (spam filters) or can't be articulated (image recognition)

**Types of ML Systems (by supervision)**
- Supervised: human-labeled data (classification = categories, regression = numbers)
- Unsupervised: no labels, finds structure (clustering, anomaly detection)
- Semi-supervised: some labels + lots of unlabeled data
- Self-supervised: auto-generates labels from data itself (why LLMs scale infinitely)
- Reinforcement: agent learns from rewards/penalties, not datasets

**Other Dimensions**
- Batch vs online learning: retrain from scratch vs learn incrementally
- Instance-based vs model-based: store examples vs learn parameters

**Main Challenges**
- Insufficient data, nonrepresentative data, poor quality data
- Irrelevant features
- Overfitting: high train score, low test score (model too complex)
- Underfitting: low train score, low test score (model too simple)

**Testing and Validation**
- Train/validation/test split: validation for tuning, test only touched once
- Cross-validation: k-fold rotation when data is limited
- Data mismatch: test set must represent production data

### Areas to Revisit
- Self-supervised vs unsupervised distinction
- The "labeled data" terminology (features vs targets)

### Spaced Repetition Questions
1. Why does self-supervised learning scale better than supervised?
2. What's the difference between classification and regression?
3. You have high training accuracy but low test accuracy. What's the problem?
4. Why do you need a validation set separate from the test set?
5. When would you use online learning instead of batch learning?
6. You train on web images, test on web images, get 97%. Users complain it doesn't work. What went wrong?

---

## Next Up: Chapter 2 - End-to-End Machine Learning Project
