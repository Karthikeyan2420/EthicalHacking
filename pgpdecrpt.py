import pgpy

# Load your private key
private_key_data = """-----BEGIN PGP PRIVATE KEY BLOCK-----
<Your PGP Private Key Here>
-----END PGP PRIVATE KEY BLOCK-----"""
private_key, _ = pgpy.PGPKey.from_blob(private_key_data)

# Encrypted PGP message
encrypted_message = """-----BEGIN PGP MESSAGE-----
<Your Encrypted Message Here>
-----END PGP MESSAGE-----"""
message = pgpy.PGPMessage.from_blob(encrypted_message)

# Decrypt the message
with private_key.unlock("<Your Private Key Passphrase>"):  # Replace with your passphrase
    decrypted_message = private_key.decrypt(message)

print("Decrypted Message:")
print(decrypted_message.message)
