import random


def pickone(classes):
    class_ = random.choice(classes)
    return class_[0](*class_[1], **class_[2])
