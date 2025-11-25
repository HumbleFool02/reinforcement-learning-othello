import sys
from absl import app, flags, logging

FLAGS = flags.FLAGS

flags.DEFINE_string("mode", None,
                    "Mode: 't' for train, 'h' for play vs human, 'm' for play vs machine.")
flags.DEFINE_string("path", None,
                    "Folder where model weights are saved or loaded.")
flags.DEFINE_float("lr", 1e-6,
                   "Learning rate (only matters for training).")
flags.DEFINE_boolean("random", True,
                     "Whether to add randomness during training.")
flags.DEFINE_integer("save_frequency", 50,
                     "How often to save during training.")
flags.DEFINE_list("load_weight", [-1],
                  "List of weight indices to load. "
                  "Length 1 for training or vs-human; length 2 for vs-machine.")
flags.DEFINE_integer("total_episodes", 10000,
                     "Number of episodes to run (training only).")

flags.mark_flag_as_required("mode")
flags.mark_flag_as_required("path")

from OthelloController import OthelloController
from OthelloAgainstAI import OthelloSession
from OthelloArena import Arena


def main(argv):
    del argv  # unused

    # normalize load_weight entries (strip [ ])
    FLAGS.load_weight = [str(w).replace('[', '').replace(']', '').strip()
                         for w in FLAGS.load_weight]

    if FLAGS.mode == 't':  # --- Training mode ---
        epsilon = 5 if FLAGS.random else 10000000
        controller = OthelloController(
            FLAGS.path, 1, learning_rate=FLAGS.lr, epsilon=epsilon)

        # skip loading if weight == -1
        lw = int(FLAGS.load_weight[0])
        if lw != -1:
            print(f"Loading model index {lw}")
            controller.load([lw])
        else:
            print("Starting fresh training (no initial weights).")

        controller.main(lw, FLAGS.total_episodes, FLAGS.save_frequency)

    elif FLAGS.mode == 'h':  # --- Human vs AI ---
        lw = int(FLAGS.load_weight[0])
        print(f"Loading model index {lw} for human vs AI play.")
        session = OthelloSession(FLAGS.path)
        session.play(lw)

    elif FLAGS.mode == 'm':  # --- AI vs AI ---
        # normalize both indices
        FLAGS.load_weight = [str(w).replace('[', '').replace(']', '').strip()
                             for w in FLAGS.load_weight]
        w1, w2 = map(int, FLAGS.load_weight)
        print(f"AI vs AI: {w1} vs {w2}")
        arena = Arena(FLAGS.path)
        arena.play(w1, w2)


if __name__ == "__main__":
    app.run(main)
