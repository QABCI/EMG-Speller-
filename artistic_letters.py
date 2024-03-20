
artistic_letters = { 
    'A': r"""
    AAAAA
   A    A
  AAAAAAA
 A        A
A          A
""",
    'B': r"""
 BBBBB
 B    B
 BBBBB
 B    B
 BBBBB
""",
    'C': r"""
  CCCCC
 C
 C
 C
  CCCCC
""",
    'D': r"""
 DDDDD
 D    D
 D    D
 D    D
 DDDDD
""",
    'E': r"""
 EEEEE
 E
 EEEE
 E
 EEEEE
""",
    'F': r"""
 FFFFF
 F
 FFFF
 F
 F
""",
    'G': r"""
  GGGGG
 G
 G  GGG
 G    G
  GGGG
""",
    'H': r"""
 H    H
 H    H
 HHHHHH
 H    H
 H    H
""",
    'I': r"""
 IIIIII
   II
   II
   II
 IIIIII
""",
    'J': r"""
     J
     J
     J
 J   J
  JJJ
""",
    'K': r"""
 K    K
 K  K
 KKK
 K  K
 K    K
""",
    'L': r"""
 L
 L
 L
 L
 LLLLL
""",
    'M': r"""
 M    M
 MM  MM
 M MM M
 M    M
 M    M
""",
    'N': r"""
 N    N
 NN   N
 N N  N
 N  N N
 N    N
""",
    'O': r"""
  OOO
 O   O
 O   O
 O   O
  OOO
""",
    'P': r"""
 PPPPP
 P    P
 PPPPP
 P
 P
""",
    'Q': r"""
  QQQ
 Q   Q
 Q   Q
 Q  QQ
  QQQ
    Q
""",
    'R': r"""
 RRRRR
 R    R
 RRRRR
 R  R
 R   RR
""",
    'S': r"""
  SSSS
 S
  SSS
     S
 SSSS
""",
    'T': r"""
 TTTTTTTT
    TT
    TT
    TT
    TT
""",
    'U': r"""
 U    U
 U    U
 U    U
 U    U
  UUUU
""",
    'V': r"""
 V     V
  V   V
   V V
    V
""",
    'W': r"""
 W     W
 W  W  W
 W  W  W
 WWWWwwW
 W     W
""",
    'X': r"""
 X     X
  X   X
    X
  X   X
 X     X
""",
    'Y': r"""
 Y     Y
  Y   Y
    Y
    Y
    Y
""",
    'Z': r"""
 ZZZZZZ
     Z
    Z
   Z
 ZZZZZZ
""",
    '*': r"""
 *    *
   * *
 * *** *
   * *
 *    *
""",
}

def print_artistic_letter(letter):#output the Letter
    if letter.upper() in artistic_letters:
        print(artistic_letters[letter.upper()])
    else:
        print(f"Artistic representation for '{letter}' not available.")