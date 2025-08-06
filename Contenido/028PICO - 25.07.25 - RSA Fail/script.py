from Crypto.PublicKey import RSA
import math

C = 13676554040830251974137947517968752293989661873871497867027766277686225433139470556608736051457164876622597482657285883515687020489538887919592727359871033
e = 65537
N = 14414021214616613071535161047503450254223173326423411873419143609549638889614180287362055403299555715248288949856529266361048703291825160015168396244917402

print(f"C = {C}")
print(f"e = {e}")
print(f"N = {N}")
print(f"N bit length: {N.bit_length()}")

# Check if C is larger than N (which would be invalid)
print(f"C > N: {C > N}")
print(f"C < N: {C < N}")

# Try to factor N (for small N this might work)
def simple_factor(n):
    """Try simple factorization methods"""
    # Check small primes
    for i in range(2, min(1000000, int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return i, n // i
    return None, None

print("Attempting to factor N...")
p, q = simple_factor(N)
if p and q:
    print(f"Found factors: p = {p}, q = {q}")
    # Calculate private exponent
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Modular inverse
    print(f"Private exponent d = {d}")
    
    # Decrypt
    M = pow(C, d, N)
    print(f"Decrypted message (decimal): {M}")
    
    # Convert to readable format
    try:
        message_bytes = M.to_bytes((M.bit_length() + 7) // 8, 'big')
        print(f"Message as bytes: {message_bytes}")
        print(f"Message as string: {message_bytes.decode('utf-8', errors='ignore')}")
    except Exception as ex:
        print(f"Could not convert to string: {ex}")
else:
    print("Could not factor N with simple methods")
    
    # Let's try another approach - check if this is a small message attack
    # Sometimes the plaintext^e is small enough that no modular reduction occurs
    def nth_root(n, k):
        """Calculate the integer nth root of k."""
        if k == 0:
            return 0
        if k == 1:
            return 1
            
        # Binary search for the nth root
        low = 0
        high = k
        
        while low <= high:
            mid = (low + high) // 2
            mid_pow = mid ** n
            
            if mid_pow == k:
                return mid
            elif mid_pow < k:
                low = mid + 1
            else:
                high = mid - 1
                
        return high  # Return the largest integer whose nth power <= k
    
    print("\nTrying small message attack (taking eth root of C)...")
    M = nth_root(e, C)
    print(f"eth root result: {M}")
    
    # Verify: M^e should equal C if this is correct
    if pow(M, e) == C:
        print("Success! M^e == C")
        try:
            message_bytes = M.to_bytes((M.bit_length() + 7) // 8, 'big')
            print(f"Message as bytes: {message_bytes}")
            print(f"Message as string: {message_bytes.decode('utf-8', errors='ignore')}")
        except Exception as ex:
            print(f"Could not convert to string: {ex}")
    else:
        print(f"M^e = {pow(M, e)} != C = {C}")
        print("Small message attack failed")
