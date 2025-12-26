# Blackjack Card Counting Simulator - Monte Carlo Analysis

A Python-based Monte Carlo simulator comparing card counting versus flat betting strategies in blackjack. Demonstrates the importance of sample size when exploiting small statistical edges.

## Project Overview

This simulator implements a complete blackjack game with the Hi-Lo card counting system and runs 100 independent trials of 10,000 hands each to analyze the statistical distribution of outcomes. The goal is to demonstrate that even with a theoretical edge, variance plays a significant role in short-term results.

### Key Features

- **Complete blackjack rules** (6-deck shoe, 3:2 blackjack payout, realistic dealer behavior)
- **Hi-Lo card counting system** with true count calculation and variable bet sizing
- **Basic strategy** for optimal play decisions
- **Monte Carlo simulation** (100 trials × 10,000 hands = 2 million hands analyzed)
- **Statistical analysis** with distribution histograms and comparative metrics

## Expected Results

Card counting typically provides a **0.5-1.5% advantage** over flat betting. Over 100 simulations:

- Card counting wins approximately **50-60% of simulations**
- Average advantage: **$50-$150 per 10,000 hands**
- Both strategies typically show negative ROI due to house edge

*Actual results vary significantly due to variance and randomness.*

## Key Learnings

### 1. Small Edges Require Large Samples
Card counting provides only a ~1% advantage. With high variance, you need tens of thousands of hands to consistently see this edge emerge. In 46% of simulations, flat betting actually outperformed card counting due to variance.

### 2. Expected Value vs. Variance
Both strategies lose money on average due to house edge, but card counting loses *less*. This demonstrates that even optimal strategies can have negative expected value depending on the game rules.

### 3. Monte Carlo Methodology
Running multiple independent trials reveals the distribution of possible outcomes rather than just a single result. This is standard practice in quantitative finance for backtesting trading strategies.

### 4. Statistical Significance
The overlapping histograms show that while card counting's distribution is slightly shifted toward better outcomes, there's substantial overlap. This visualizes why "beating the house" isn't guaranteed even with perfect play.

### 5. Risk Management
Even with card counting, bankroll variance is significant. The results ranged from ~$4,000 to ~$12,000 across different simulations, highlighting the importance of proper bankroll management.

## Technical Implementation

**Card Counting (Hi-Lo System)**:
- Low cards (2-6): +1
- Neutral cards (7-9): 0  
- High cards (10-A): -1
- True Count = Running Count ÷ Decks Remaining
- Bet spread: 1-4 units based on true count

**Basic Strategy**:
- Always hit on 11 or below
- Stand on 17 or above
- Hit on 12-16 if dealer shows 7+
- Double down on 10-11 against dealer 2-9

**Simulation Parameters**:
- Starting bankroll: $10,000
- Base bet: $10
- Hands per simulation: 10,000
- Number of simulations: 100

## Future Enhancements

### Advanced Counting Systems
- Implement Omega II, Hi-Opt I/II, or Zen Count for comparison
- Analyze betting correlation vs. playing efficiency tradeoffs
- Test unbalanced counts (KO, Red 7)

### Bet Sizing Optimization
- Kelly Criterion for mathematically optimal bet sizing
- Risk of Ruin calculations at different bankroll levels
- Comparison of aggressive vs. conservative bet spreads

### Rule Variations
- Different dealer rules (Hit at 17 vs Stand at 17)
- Surrender option analysis
- Double after split (DAS) impact
- Multiple deck configurations (1, 2, 6, 8 decks)

### Advanced Analytics
- Bankroll drawdown analysis
- Win/loss streak distributions  
- Session length optimization
- Heat management simulation (avoiding casino detection)

### Visualization Improvements
- Real-time animated bankroll progression
- Interactive dashboard with adjustable parameters
- Heatmaps showing profitability by count
- Confidence intervals on distribution plots

### Team Play Simulation
- Multiple player coordination
- Big player + spotters strategy
- Profit splitting analysis

### Machine Learning Extension - Strategy Evolution

**Reinforcement Learning Strategy Optimizer**: Train an AI agent that evolves its blackjack strategy across 100 simulations to discover optimal play patterns.

**How it would work**:
- Agent starts with random or basic playing decisions
- Each simulation, the agent tries different strategies (when to hit, stand, double)
- Agent receives rewards for wins and penalties for losses
- Strategy evolves based on which decisions led to better outcomes
- After 100 iterations, compare ML-discovered strategy vs. traditional basic strategy

**Potential approaches**:
- **Q-Learning**: Learn value of each action (hit/stand/double) for every game state
- **Deep Q-Network (DQN)**: Use neural network to handle large state space
- **Genetic Algorithm**: Evolve strategy rules that perform best across generations
- **Policy Gradient**: Directly optimize playing decisions to maximize expected profit

**Expected insights**:
- Can ML discover strategies superior to human-designed basic strategy?
- How quickly does the agent converge to optimal play?
- Does the learned strategy differ significantly from traditional approaches?
- Comparison of ML strategy vs. card counting vs. basic strategy performance

**Implementation challenges**:
- Defining state space (hand value, dealer card, count, deck penetration)
- Balancing exploration (trying new strategies) vs. exploitation (using known good strategies)
- Handling the credit assignment problem (which decisions led to wins/losses?)
- Training time for convergence (may require millions of hands)

## Technologies Used

- **Python 3.x**: Core simulation logic
- **Matplotlib**: Statistical visualization and histograms
- **Random**: Deck shuffling and probabilistic outcomes

---

**Disclaimer**: Educational project only. Card counting is legal but casinos may refuse service to advantage players.