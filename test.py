import tensorflow as tf
import tensorflow_probability as tfp
import gym
import argparse
import numpy as np
import collections
import matplotlib.pyplot as plt

Trans = collections.namedtuple("Trans", ["state", "action", "reward", "next_state", "done"])

class Estimator():
    def __init__(self, env, learning_rate = 0.02):
        self.state = tf.placeholder(tf.float32, env.observation_space.shape, name="state")
        self.action = tf.placeholder(dtype=tf.int32, name="action")
        self.G = tf.placeholder(dtype=tf.float32, name="G")

        self.hidden_layer1 = tf.contrib.layers.fully_connected(
            inputs = tf.expand_dims(self.state, 0),
            num_outputs = 256,
            activation_fn = tf.nn.relu, 
            weights_initializer = tf.zeros_initializer)

        self.hidden_layer2 = tf.contrib.layers.fully_connected(
            inputs = self.hidden_layer1,
            num_outputs = 64,
            activation_fn = tf.nn.relu, 
            weights_initializer = tf.zeros_initializer)

        self.hidden_layer3 = tf.contrib.layers.fully_connected(
            inputs = self.hidden_layer2,
            num_outputs = 16,
            activation_fn = tf.nn.relu, 
            weights_initializer = tf.zeros_initializer)

        self.output_layer = tf.contrib.layers.fully_connected(
            inputs = self.hidden_layer3,
            num_outputs = env.action_space.n,
            activation_fn = None, #tf.nn.relu, 
            weights_initializer = tf.zeros_initializer)

        self.action_probs = tf.squeeze(tf.nn.softmax(self.output_layer))
        self.selected_action_prob = tf.gather(self.action_probs, self.action)

        self.loss = -tf.log(self.selected_action_prob) * self.G
        self.optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
        self.train_op = self.optimizer.minimize(self.loss, global_step = tf.contrib.framework.get_global_step())

    def predict_action(self, state, sess = None):
        sess = sess or tf.get_default_session()
        return sess.run(self.action_probs, {self.state:state})

    def update_policy(self, state, G, action, sess = None):
        sess = sess or tf.get_default_session()
        feed_dict = {self.state:state, self.G:G, self.action:action}
        _, loss = sess.run([self.train_op, self.loss], feed_dict)
        return loss

# Sample documentation
def sample_func(a, b):
    """
    compute a plus b
    :param a: an integer
    :param b: an integer
    :return: c=a+b, an integer
    """
    return a+b

def generate_samples(env, estimator, learning_rate = 0.01):
    """
    :param env: the current environment
    :param estimator: an estimator
    :param learning_rate: learning rate, 0.01 by default
    :return: total reward, total number of step of the episode, and a list of trajectroies as the episode
    """
    state = env.reset()
    episode = []
    episode_reward = 0
    step = 0
    while (1==1):
        action_probs = estimator.predict_action(state)
        action = np.random.choice(np.arange(len(action_probs)), p = action_probs)
        next_state, reward, done, _ = env.step(action)

        episode.append(Trans(state = state, action = action, reward = reward, next_state = next_state, done = done))

        episode_reward += reward

        if done:
            break

        state = next_state
        step += 1

    return episode_reward, step, episode


def estimate_return(episode, estimator, discount_factor = 0.3):
    """
    :param episode: a list of transitions of an episode
    :param estimator: a policy estimator
    :param discount_factor: gamma, 0.8 by default
    :return: a list of returns (G) for each step in the episode
    """
    returns = []
    for step, transition in enumerate(episode):
        current_G = sum([discount_factor**i * t.reward for i,t in enumerate(episode[step:])])
        returns.append(current_G)

    return returns


def update_policy(episode, returns, estimator):
    """
    :param episode: a list of transitions of an episode
    :param returns: corresponding returns of each step
    :param estimator: a policy estimator
    """
    total_loss = 0
    for current_G, transition in zip(returns, episode):
        total_loss += estimator.update_policy(transition.state, current_G, transition.action)
    return total_loss / len(episode)


#TODO
# Any other functions you need

def main(args):
    env = gym.make(args.env)

    #TODO
    #Your own initialization
    with tf.Session() as sess:
        estimator = Estimator(env)
        sess.run(tf.initialize_all_variables())
        rewards = []
        lengths = []
        losses = []

        for i in range(args.n_iter):
            reward, length, episode = generate_samples(env, estimator)

            returns = estimate_return(episode, estimator)

            loss = update_policy(episode, returns, estimator)

            # print or log some statistics for debug and evaluation
            print("Episode {}/{}".format(i, args.n_iter))
            rewards.append(reward)
            lengths.append(length)
            losses.append(loss)

    plt.plot(lengths)
    plt.plot(rewards, "r")
    plt.show()
    plt.plot(losses)
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("env", type=str)
    parser.add_argument("--n_iter", type=int, default=100)
    #TODO
    # add your own parameters

    main(parser.parse_args())
