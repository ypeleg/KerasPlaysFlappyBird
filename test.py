from model import model
from qlearning4k import Agent
from flappy_bird import FlappyBird

game = FlappyBird(frame_rate=30, sounds=True)
model.load_weights('weights.dat')
agent = Agent(model)
agent.play(game, nb_epoch=100, epsilon=0.01, visualize=False)
