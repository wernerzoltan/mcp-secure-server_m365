"""
What is JWKS?
JWKS stands for JSON Web Key Set. It is a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by the authorization server and signed using the RS256 or other asymmetric algorithms. Each key in the set is represented as a JSON object and contains information such as the key type, key ID, and the actual public key material.

Real OAuth providers publish something similar to:
{
  "keys": [
    {
      "kty": "RSA",
      "kid": "1b94c",
      "use": "sig",
      "n": "vrjOf...",
      "e": "AQAB"
    }
  ]
}
Clients use this information to validate JWT signatures.
"""

"""
Mock JWKS document.

Development only.
No real cryptographic keys.
"""


MOCK_JWKS = {
    "keys": [
        {
            "kid": "mock-key-id",
            "kty": "RSA",
            "alg": "RS256",
            "use": "sig",
        }
    ]
}