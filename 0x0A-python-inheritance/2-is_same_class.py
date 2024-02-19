#!/usr/bin/python3
""" defining a function is_same_class """


def is_same_class(obj, a_class):
    """checking if obj is exactly an instance of a_class"""
    return type(obj) == a_class
