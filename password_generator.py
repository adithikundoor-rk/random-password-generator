import math
import secrets
import string

# --- MODEL (Core Cryptographic & Analytical Logic) ---

def calculate_entropy(length, pool_size):
    """
    Applies the mathematical information entropy formula: E = L * log2(R)
    Proves the strength of the credential against modern cracking hardware.
    """
    if pool_size <= 0 or length <= 0:
        return 0.0
    return length * math.log2(pool_size)

def generate_secure_credential(length):
    """
    Enterprise-grade transformation engine.
    Ensures O(N) linear time complexity and cryptographic randomness.
    """
    # Standardizing character classification via Python's locale-independent string module
    character_pool = string.ascii_letters + string.digits + string.punctuation
    pool_size = len(character_pool)
    
    # Utilizing an optimized array/list to eliminate string immutability memory overhead
    password_buffer = []
    
    for _ in range(length):
        # Accessing highest-quality OS hardware-level noise (entropy sources)
        secure_char = secrets.choice(character_pool)
        password_buffer.append(secure_char)
        
    # Assembling character fragments efficiently in a single memory allocation sweep
    final_password = "".join(password_buffer)
    
    # Compute security metrics
    entropy_bits = calculate_entropy(length, pool_size)
    
    return final_password, entropy_bits


# --- VIEW & CONTROLLER (Input Validation & Display) ---

def run_credential_engine():
    """Manages the Input-Process-Output scaffold loop."""
    print("\n" + "="*55)
    print("    DECODELABS ENTERPRISE CREDENTIAL SECURITY CORE   ")
    print("="*55)
    
    while True:
        # Phase 1: Environmental Requirements and Data Validation (The Gate)
        user_input = input("\nEnter desired password length (or 'exit' to close): ").strip()
        
        if user_input.lower() == 'exit':
            print("\nShutting down security core gracefully. Stay protected.")
            break
            
        try:
            target_length = int(user_input)
            
            # Implementing rigid validation barriers inspired by modern NIST guidelines
            if target_length < 8:
                print("[X] Security Policy Violation: Minimum length must be at least 8 characters.")
                continue
            elif target_length < 15:
                print("[!] Notice: NIST guidelines recommend 15+ characters for maximum security.")
                
            # Phase 2 & 3: Process & Output Execution Path
            password, entropy = generate_secure_credential(target_length)
            
            print("\n" + "—"*55)
            print(f" GENERATED CREDENTIAL :  {password}")
            print(f" SYSTEM ENTROPY VALUE :  {entropy:.2f} Bits")
            
            # Map structural hardness metrics for human operators
            if entropy < 60:
                print(" SECURITY HARDNESS    :  WEAK (Susceptible to modern GPU clusters)")
            elif entropy < 80:
                print(" SECURITY HARDNESS    :  MODERATE (Standard protection)")
            else:
                print(" SECURITY HARDNESS    :  STRONG (Enterprise Compliant)")
            print("—"*55)
            
        except ValueError:
            print("[X] Structural Error: Input stream must resolve to a valid base-10 integer.")

if __name__ == "__main__":
    run_credential_engine()