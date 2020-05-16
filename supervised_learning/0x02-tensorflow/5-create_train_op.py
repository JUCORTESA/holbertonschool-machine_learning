#!/usr/bin/env python3
"""Train"""
import tensorflow as tf


def create_train_op(loss, alpha):
    """
    Creates the training operation for the network
    :param loss: is the loss of the network’s prediction
    :param alpha: is the learning rate
    :return: an operation that trains the network using gradient descent
    """
    return tf.train.GradientDescentOptimizer(alpha).minimize(loss)
