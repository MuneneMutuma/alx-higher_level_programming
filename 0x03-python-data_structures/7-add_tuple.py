#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first, second = 0, 0
    try:
        first += tuple_a[0]
    try:
        first += tuple_b[0]
    try:
        second += tuple_a[1]
    try:
        second += tuple_b[1]

    return first, second
