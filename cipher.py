ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def vigenere(text: str, key: str, encrypt: bool = True) -> str:
    """Core algorithm — encrypt or decrypt using the Vigenère method.

    Encrypt: ci = (pi + ki) % 26
    Decrypt: ci = (pi - ki + 26) % 26
    """
    k = [c for c in key.upper() if c.isalpha()]
    if not k:
        return text
    result, ki = [], 0
    for ch in text:
        if not ch.isalpha():
            result.append(ch)           # spaces/punctuation unchanged
            continue
        pi    = ALPHA.index(ch.upper())
        shift = ALPHA.index(k[ki % len(k)])
        ki   += 1
        ci    = (pi + shift) % 26 if encrypt \
                else (pi - shift + 26) % 26
        out   = ALPHA[ci]
        result.append(out.lower() if ch.islower() else out)
    return "".join(result)


def encrypt(text: str, key: str) -> str:
    return vigenere(text, key, True)

def decrypt(text: str, key: str) -> str:
    return vigenere(text, key, False)


def build_tableau() -> list:
    """26×26 grid — row = plain letter, col = key letter."""
    return [[ALPHA[(r + c) % 26] for c in range(26)]
            for r in range(26)]


def print_tableau():
    print("   " + " ".join(ALPHA))
    for i, row in enumerate(build_tableau()):
        print(ALPHA[i] + "  " + " ".join(row))


def step_trace(text: str, key: str, enc: bool):
    """Print a character-by-character substitution trace."""
    k = [c for c in key.upper() if c.isalpha()]
    ki = 0
    for ch in text:
        if not ch.isalpha():
            print(f"  '{ch}' → '{ch}'  (unchanged)")
            continue
        pi    = ALPHA.index(ch.upper())
        kch   = k[ki % len(k)]
        shift = ALPHA.index(kch)
        ci    = (pi + shift) % 26 if enc else (pi - shift + 26) % 26
        formula = f"({pi}+{shift})%26={ci}" if enc else f"({pi}-{shift}+26)%26={ci}"
        print(f"  '{ch.upper()}' key='{kch}' → '{ALPHA[ci]}'  [{formula}]")
        ki += 1


def interactive_menu():
    banner = """
╔═══════════════════════════════════╗
║      VIGENÈRE CIPHER              ║
║  Polyalphabetic substitution      ║
╚═══════════════════════════════════╝"""
    print(banner)
    while True:
        print("\n  1 — Encrypt\n  2 — Decrypt"
              "\n  3 — Show tableau\n  4 — Step trace\n  0 — Exit")
        choice = input("  Choose: ").strip()
        if choice == "0":
            break
        elif choice in ("1", "2"):
            enc = choice == "1"
            t   = input(f"  {'Plain' if enc else 'Cipher'}text: ")
            k   = input("  Key            : ")
            out = encrypt(t, k) if enc else decrypt(t, k)
            label = "Ciphertext" if enc else "Plaintext "
            print(f"  {label}: {out}")
        elif choice == "3":
            print_tableau()
        elif choice == "4":
            mode = input("  Mode [encrypt/decrypt]: ").strip().lower()
            t    = input("  Text: ")
            k    = input("  Key : ")
            step_trace(t, k, mode == "encrypt")


if __name__ == "__main__":
    interactive_menu()
