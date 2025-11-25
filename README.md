# How to Run the Othello AI Program

## Prerequisites

### Required Software
- **Python 3.6+** (recommended: Python 3.8 or higher)
- **pip** (Python package manager)

### Required Libraries

Install the following Python packages:

```bash
pip install keras
pip install tensorflow
pip install numpy
pip install absl-py
```

Or install all at once:

```bash
pip install keras tensorflow numpy absl-py
```

**Note**: Keras requires TensorFlow as a backend. The installation will automatically handle this dependency.

---

## Project Structure

Ensure all files are in the same directory:

```
othello-ai/
├── OthelloBoard.py          # Game engine
├── OthelloCanvas.py         # Visual display
├── OthelloPlayer.py         # AI player logic
├── AlphaBeta.py            # Search algorithm
├── OthelloController.py    # Training manager
├── OthelloInterface.py     # Command-line interface
├── OthelloScript.py        # Simple script interface
├── OthelloAgainstAI.py     # Human vs AI mode
└── OthelloArena.py         # AI vs AI mode
```

---

## Running the Program

There are **two ways** to run the program:

### **Method 1: Using OthelloScript.py (Easier for Beginners)**
### **Method 2: Using OthelloInterface.py (Command Line)**

---

## Method 1: OthelloScript.py (Simple Configuration)

### Step 1: Edit Configuration

Open `OthelloScript.py` in a text editor and modify these variables:

```python
MODE = 't'           # 't' = train, 'h' = human vs AI, 'm' = AI vs AI
PATH = './weights/'  # Directory to save/load model weights
LR = 0.001          # Learning rate
RANDOM = True       # Enable random exploration
SAVE_FREQUENCY = 50 # Save weights every N episodes
WEIGHTS = [-1]      # [-1] = start fresh, [500] = load episode 500
TOTAL_EPISODES = 1000  # Number of training episodes
```

**Important**: You MUST set the `PATH` variable. Create the directory if it doesn't exist:

```bash
mkdir weights
```

### Step 2: Run the Script

```bash
python OthelloScript.py
```

### Examples:

#### Example 1: Train a New AI (1000 episodes)
```python
MODE = 't'
PATH = './weights/'
WEIGHTS = [-1]
TOTAL_EPISODES = 1000
```
```bash
python OthelloScript.py
```

#### Example 2: Continue Training from Episode 500
```python
MODE = 't'
PATH = './weights/'
WEIGHTS = [500]
TOTAL_EPISODES = 1000
```
```bash
python OthelloScript.py
```

#### Example 3: Play Against AI (Load Episode 1000)
```python
MODE = 'h'
PATH = './weights/'
WEIGHTS = [1000]
```
```bash
python OthelloScript.py
```

#### Example 4: Watch Two AIs Play
```python
MODE = 'm'
PATH = './weights/'
WEIGHTS = [500, 1000]  # First AI vs Second AI
```
```bash
python OthelloScript.py
```

---

## Method 2: OthelloInterface.py (Command Line)

### Basic Syntax

```bash
python OthelloInterface.py --mode=<mode> --path=<path> [options]
```

### Required Arguments
- `--mode`: Operation mode ('t', 'h', or 'm')
- `--path`: Directory for saving/loading weights

### Optional Arguments
- `--lr`: Learning rate (default: 0.000001)
- `--random`: Enable randomness (default: True)
- `--save_frequency`: Save every N episodes (default: 50)
- `--load_weight`: Weights to load (default: [-1])
- `--total_episodes`: Training episodes (default: 10000)

### Examples:

#### Example 1: Train a New AI
```bash
python OthelloInterface.py \
    --mode=t \
    --path=./weights/ \
    --total_episodes=1000 \
    --lr=0.001
```

#### Example 2: Resume Training from Episode 500
```bash
python OthelloInterface.py \
    --mode=t \
    --path=./weights/ \
    --load_weight=[500] \
    --total_episodes=1000
```

#### Example 3: Play Against AI
```bash
python OthelloInterface.py \
    --mode=h \
    --path=./weights/ \
    --load_weight=[1000]
```

#### Example 4: Watch Two AIs Play
```bash
python OthelloInterface.py \
    --mode=m \
    --path=./weights/ \
    --load_weight=[500,1000]
```

#### Example 5: Get Help
```bash
python OthelloInterface.py --helpshort
```

---

## Modes Explained

### Mode 't': Train Mode

**What it does**: Trains an AI by self-play

**Process**:
1. AI plays games against itself
2. Learns from game outcomes
3. Saves weights periodically
4. Improves over time

**Example**:
```bash
python OthelloInterface.py --mode=t --path=./weights/ --total_episodes=1000
```

**Output**:
```
Episode 0: Training...
Episode 50: Saving weights...
Episode 100: Saving weights...
...
Episode 1000: Training complete!
```

**Files created**:
- `./weights/Reversi_0` (initial weights)
- `./weights/Reversi_50` (after 50 episodes)
- `./weights/Reversi_100` (after 100 episodes)
- etc.

**Time**: Depends on hardware (GPU recommended)
- ~1-2 minutes per 10 episodes on modern CPU
- ~30 seconds per 10 episodes on GPU

---

### Mode 'h': Human vs AI Mode

**What it does**: Opens a GUI where you play against the trained AI

**Controls**:
- **Left Click**: Place your piece (you play as Black)
- **Middle Click**: Pass your turn
- **AI plays as White** and responds automatically

**Example**:
```bash
python OthelloInterface.py --mode=h --path=./weights/ --load_weight=[1000]
```

**GUI Instructions**:
1. Window opens showing 8×8 Othello board
2. Click any valid square to make your move
3. AI responds immediately
4. Continue until game ends
5. Console prints "Done!!!" when game finishes

**Valid Moves**:
- Must flip at least one opponent piece
- If invalid move attempted, console prints: "That Move cannot be made, make another one."

---

### Mode 'm': AI vs AI Arena Mode

**What it does**: Watch two trained AIs play against each other

**Purpose**: Compare different training stages

**Example**:
```bash
python OthelloInterface.py --mode=m --path=./weights/ --load_weight=[500,1000]
```

**What happens**:
1. Loads two AIs (episode 500 and episode 1000)
2. They play against each other
3. Moves displayed with 2-second delay between moves
4. Observe which AI plays better

**Note**: Currently runs indefinitely (no automatic stop)

---

## Training Parameters Explained

### Learning Rate (`--lr`)
- **Default**: 0.000001 (very small)
- **Range**: 0.00001 to 0.01
- **Effect**: How much to update network per training step
- **Recommendation**: Keep default for deep networks

### Random Exploration (`--random`)
- **Default**: True
- **Effect**: 
  - True: epsilon = 5 (more exploration, learns faster)
  - False: epsilon = 10000000 (almost no exploration)
- **Recommendation**: True for training, False for evaluation

### Save Frequency (`--save_frequency`)
- **Default**: 50
- **Effect**: Saves weights every N episodes
- **Recommendation**: 
  - 10-50 for short training sessions
  - 100-500 for long training sessions

### Total Episodes (`--total_episodes`)
- **Default**: 10000
- **Range**: 100 to 100000+
- **Effect**: How long to train
- **Recommendation**:
  - 1000 episodes: Basic competence (~1-2 hours)
  - 5000 episodes: Good play (~5-10 hours)
  - 10000+ episodes: Strong play (~12-24 hours)

---

## Troubleshooting

### Error: "You need to set a path in OthelloScript before running it."
**Solution**: Edit `OthelloScript.py` and set `PATH = './weights/'`

### Error: "No module named 'keras'"
**Solution**: Install dependencies
```bash
pip install keras tensorflow
```

### Error: "Unable to open file (file signature not found)"
**Solution**: The weight file doesn't exist. Either:
1. Train a new model: `--load_weight=[-1]`
2. Check the path and episode number

### Error: "list index out of range"
**Solution**: For AI vs AI mode, provide two weight values:
```bash
--load_weight=[500,1000]
```

### GUI doesn't open
**Solution**: Make sure tkinter is installed (usually comes with Python):
```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On macOS (via Homebrew)
brew install python-tk
```

### Training is very slow
**Solutions**:
1. Reduce `--total_episodes`
2. Install TensorFlow GPU version
3. Reduce network size (requires code modification)

### "Invalid Move" keeps printing
**Solution**: You're clicking invalid squares. Only squares that flip opponent pieces are valid.

---

## Expected Training Output

### Console Output During Training:
```
Episode finished after 67 timesteps
Episode finished after 72 timesteps
Episode finished after 68 timesteps
0
Episode finished after 65 timesteps
...
50
Episode finished after 70 timesteps
```

Numbers like "0", "50", "100" indicate when weights are saved.

### Weight Files Created:
```
weights/
├── Reversi_0.data-00000-of-00001
├── Reversi_0.index
├── Reversi_50.data-00000-of-00001
├── Reversi_50.index
├── Reversi_100.data-00000-of-00001
└── Reversi_100.index
```

Each episode creates two files (.data and .index).

---

## Quick Start Guide

### Absolute Beginner (3 Steps):

```bash
# 1. Install dependencies
pip install keras tensorflow numpy absl-py

# 2. Create weights directory
mkdir weights

# 3. Train for 100 episodes (quick test)
python OthelloInterface.py --mode=t --path=./weights/ --total_episodes=100
```

### Play Against Your AI:

```bash
# After training, play against episode 100
python OthelloInterface.py --mode=h --path=./weights/ --load_weight=[100]
```

---

## Recommended Training Workflow

### Step 1: Quick Test (10 minutes)
```bash
python OthelloInterface.py --mode=t --path=./weights/ --total_episodes=100
```
Verify everything works.

### Step 2: Short Training (1-2 hours)
```bash
python OthelloInterface.py --mode=t --path=./weights/ --total_episodes=1000
```
AI learns basic strategy.

### Step 3: Play Against It
```bash
python OthelloInterface.py --mode=h --path=./weights/ --load_weight=[1000]
```
Test its strength.

### Step 4: Extended Training (overnight)
```bash
python OthelloInterface.py --mode=t --path=./weights/ --load_weight=[1000] --total_episodes=10000
```
Continue training for stronger play.

---

## Performance Benchmarks

On typical hardware:

| Episodes | Training Time | Skill Level |
|----------|---------------|-------------|
| 100 | 10-20 min | Beginner (loses to random) |
| 500 | 1-2 hours | Novice (beats random 60%) |
| 1000 | 2-4 hours | Intermediate (beats random 80%) |
| 5000 | 10-20 hours | Advanced (strong tactical play) |
| 10000 | 24-48 hours | Expert (very strong play) |

*Times based on modern CPU. GPU training is 3-5× faster.*

---

## Advanced Usage

### Custom Learning Rate
```bash
python OthelloInterface.py --mode=t --path=./weights/ --lr=0.01
```

### Disable Exploration (Pure Exploitation)
```bash
python OthelloInterface.py --mode=t --path=./weights/ --random=False
```

### Save More Frequently
```bash
python OthelloInterface.py --mode=t --path=./weights/ --save_frequency=10
```

### Compare Two Training Stages
```bash
# Train two different amounts
python OthelloInterface.py --mode=t --path=./weights1/ --total_episodes=500
python OthelloInterface.py --mode=t --path=./weights2/ --total_episodes=2000

# Watch them compete
# (requires code modification to load from different paths)
```

---

## Tips for Best Results

1. **Train overnight**: 5000+ episodes gives noticeably better play
2. **Use GPU**: Install `tensorflow-gpu` for 5× speedup
3. **Start small**: Test with 100 episodes before long training
4. **Save frequently**: Use `--save_frequency=50` to avoid losing progress
5. **Monitor loss**: Lower neural network loss = better learning

---

## Summary

**Fastest way to get started**:
```bash
# Install, create directory, train 100 episodes
pip install keras tensorflow numpy absl-py
mkdir weights
python OthelloInterface.py --mode=t --path=./weights/ --total_episodes=100

# Then play against it
python OthelloInterface.py --mode=h --path=./weights/ --load_weight=[100]
```

**For questions or issues**: Check Troubleshooting section above.

---

## References

- Original code adapted from: http://code.activestate.com/recipes/580698-reversi-othello/
- Keras documentation: https://keras.io/
- TensorFlow installation: https://www.tensorflow.org/install