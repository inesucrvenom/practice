"""trying third approach, inspired by
https://blog.valerauko.net/2018/02/11/munching-the-squares-of-immortality/

split matrix into
A B
C D
- A is max 2**k x 2**k matrix that fits into it, use direct formula
- B and C have one size 2**k, so use num_rows * sum_row idea but, be careful
    about up to where sum_row is fixed and when it changes
    - current suspicion - for each p, 2**k+p * 2**k+p
- repeat full process for D part

- don't forget to account for small mods and sum_row formula
- think if OFFSET table brings value for small submatrices (B, C, D)
"""


def initialise(l, t):
    """
    will initialise
    - MODULO, LOSS : int, global constants
    """
    global MODULO, LOSS

    MODULO = t
    LOSS = l


def apply_mod(num):
    """ simplifies writing of modulo num """
    return num % MODULO


def apply_loss_mod(num):
    """ simplifies writing of modulo loss """
    tmp = num - LOSS
    tmp = tmp if tmp > 0 else 0
    return apply_mod(tmp)
