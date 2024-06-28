from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    if my_int1>my_int2:
      return [Output(my_int1, "bigger_number", party1)]
    else:
      return [Output(my_int2, "bigger_number", party1)]


