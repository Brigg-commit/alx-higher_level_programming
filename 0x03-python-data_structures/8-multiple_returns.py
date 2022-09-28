#!/usr/bin/python3
def multiple_returns(sentence):
    for c in range(len(sentence)):
        length = len(sentence)
        if (length) == 0:
            sentence[0] = None
            return
        else:
            res = (length, sentence[0])
            return res
