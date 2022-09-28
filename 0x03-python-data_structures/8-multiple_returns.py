#!/usr/bin/python3
def multiple_returns(sentence):
    length = multiple_returns(sentence)
    if (length) == 0:
        result = (sentence[0], None)
        return result
    else:
        res = (length, sentence[0])
        return res
