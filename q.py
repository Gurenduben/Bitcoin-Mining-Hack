import ecdsa
# Enter the private key
private_key_hex = input("Enter the private key in hexadecimal format: ")

# Convert the private key to an integer
private_key_int = int(private_key_hex, 16)

# Create the SECP256k1 curve object
secp256k1_curve = ecdsa.curves.SECP256k1

# Create the private key object
private_key = ecdsa.SigningKey.from_secret_exponent(private_key_int, curve=secp256k1_curve)

# Calculate the corresponding public key for the original private key
public_key = private_key.get_verifying_key()

# Print the original private key and public key
print("Private Key: ", private_key.to_string().hex())
print("Public Key: ", public_key.to_string().hex())

# Add the private key to itself and calculate the corresponding public keys for each resulting private key
for i in range(1, 100):  # Change 5 to any number of resulting private keys you want to generate
    new_private_key_int = private_key_int + i
    new_private_key = ecdsa.SigningKey.from_secret_exponent(new_private_key_int, curve=secp256k1_curve)
    new_public_key = new_private_key.get_verifying_key()
    print("Private Key " + str(i) + ": ", new_private_key.to_string().hex())
    print("Public Key " + str(i) + ": ", new_public_key.to_string().hex())
  
