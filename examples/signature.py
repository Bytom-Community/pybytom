#!/usr/bin/env python3

from bytom.signature import sign, verify

# Bytom private key and public key
PRIVATE_KEY = "e07af52746e7cccd0a7d1fba6651a6f474bada481f34b1c5bab5e2d71e36ee51580" \
              "3ee0a6682fb19e279d8f4f7acebee8abd0fc74771c71565f9a9643fd77141"
PUBLIC_KEY = "91ff7f525ff40874c4f47f0cab42e46e3bf53adad59adef9558ad1b6448f22e2"
# Message data
MESSAGE = "1246b84985e1ab5f83f4ec2bdf271114666fd3d9e24d12981a3c861b9ed523c6"

# Signing message by private key
signature = sign(private=PRIVATE_KEY, message=MESSAGE)
print("Signature:", signature)

# Verifying signature by public key
verified = verify(public=PUBLIC_KEY, signature=signature, message=MESSAGE)
print("Verified:", verified)
