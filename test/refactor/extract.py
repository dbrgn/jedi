# --- simple
def test():
    #? 25 a
    return test(1, (30 + b, c) + 1)

# +++
def test():
    a = (30 + b, c) + 1
    return test(a)

# --- multiline
def test():
    #? 30 x
    return test(1, (30 + b, c) + 1)
# +++
def test():
    x = (30 + b, c) + 1
    return test(x)