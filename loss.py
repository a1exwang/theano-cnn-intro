import theano.tensor as T


class CrossEntropyLoss(object):
    def __init__(self, name):
        self.name = name

    def forward(self, inputs, labels):
        # Your codes here
        # hint: labels are already in one-hot form
        return -T.mean(labels * T.log(inputs) + (1-labels) * T.log(1-inputs))
