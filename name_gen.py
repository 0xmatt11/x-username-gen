import random
import string

# --- WORD BANKS ---
TECH_PREFIXES = ["sys", "net", "0x", "root", "dev", "node", "bit", "data", "cyber", "hyper"]
TECH_SUFFIXES = ["_log", "daemon", "sec", "box", "stack", "flow", "core", "shell", "v2", "ops"]

AESTHETIC_WORDS = ["luna", "nova", "flux", "zen", "aura", "echo", "mist", "velvet", "void", "sky"]

# Leetspeak dictionary for "Hacker" mode
LEET_MAP = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}

def get_user_input():
    print("\n--- 🐦 TWITTER HANDLE GENERATOR ---")
    base = input("1. Enter a base word or name (Press Enter for random): ").strip().replace(" ", "")
    
    print("\n2. Choose a Style:")
    print("   [1] Cyber / Security (e.g., 0xGemini, Net_User)")
    print("   [2] Minimalist / Short (e.g., gmni_, usr)")
    print("   [3] Chaotic / Anonymous (e.g., user_8392, x_z9)")
    style = input("   > Choice (1-3): ").strip()
    
    nums = input("\n3. Include numbers? (y/n): ").lower().strip() == 'y'
    underscores = input("4. Use underscores? (y/n): ").lower().strip() == 'y'
    
    return base, style, nums, underscores

def to_leet(text):
    """Converts text to partial leetspeak."""
    new_text = ""
    for char in text:
        if char.lower() in LEET_MAP and random.random() > 0.5: # 50% chance to convert
            new_text += LEET_MAP[char.lower()]
        else:
            new_text += char
    return new_text

def remove_vowels(text):
    """Removes vowels for minimalist look."""
    return "".join([c for c in text if c.lower() not in 'aeiou'])

def generate_cyber(base, use_nums, use_under):
    """Generates Tech/Security style names."""
    options = []
    
    # If no base provided, pick a random tech word
    if not base:
        base = random.choice(TECH_PREFIXES)

    # Strategy 1: Prefix + Base
    p = random.choice(TECH_PREFIXES)
    sep = "_" if use_under else ""
    options.append(f"{p}{sep}{base}")

    # Strategy 2: Base + Suffix
    s = random.choice(TECH_SUFFIXES)
    sep = "_" if use_under else ""
    options.append(f"{base}{sep}{s}")

    # Strategy 3: "0x" Hex style
    if use_nums:
        hex_val = random.choice(["0x", "x"])
        options.append(f"{hex_val}{base}")

    return options

def generate_minimalist(base, use_nums, use_under):
    """Generates clean, short names."""
    options = []
    if not base:
        base = random.choice(AESTHETIC_WORDS)
    
    # Strategy 1: Vowel removal (e.g., "Gmni")
    short_base = remove_vowels(base)
    options.append(short_base)
    
    # Strategy 2: Underscore wrapper
    if use_under:
        options.append(f"_{base}_")
        options.append(f"{base}_")
    
    # Strategy 3: Just lower case
    options.append(base.lower())

    return options

def generate_chaotic(base, use_nums, use_under):
    """Generates random, anonymous looking names."""
    options = []
    if not base:
        # Generate random string
        base = ''.join(random.choices(string.ascii_lowercase, k=4))

    # Strategy 1: Random ID append
    if use_nums:
        rid = random.randint(100, 9999)
        sep = "_" if use_under else ""
        options.append(f"{base}{sep}{rid}")

    # Strategy 2: Scramble caps
    scramble = "".join([c.upper() if random.random() > 0.5 else c.lower() for c in base])
    options.append(scramble)

    return options

def main():
    base, style, use_nums, use_under = get_user_input()
    
    results = set() # Use a set to avoid duplicates
    
    print(f"\n✨ Generating 20 candidates for '{base or 'Random'}'...\n")

    # Loop until we have enough results
    while len(results) < 20:
        if style == '1':
            new_batch = generate_cyber(base, use_nums, use_under)
        elif style == '2':
            new_batch = generate_minimalist(base, use_nums, use_under)
        elif style == '3':
            new_batch = generate_chaotic(base, use_nums, use_under)
        else:
            # Default fallback
            new_batch = generate_cyber(base, use_nums, use_under)
        
        # Add batch to results
        for name in new_batch:
            # Apply Leetspeak randomly if style is Cyber or Chaotic
            if style in ['1', '3'] and random.random() > 0.7:
                name = to_leet(name)
            
            # Enforce Twitter Length Limit (15 chars)
            if len(name) <= 15:
                results.add(name)

    # Print nicely
    for i, name in enumerate(results, 1):
        print(f"{i:02}. @{name}")

    print("\n💡 NOTE: This tool only generates text strings. You must manually check if they are available on X.")

if __name__ == "__main__":
    main()
