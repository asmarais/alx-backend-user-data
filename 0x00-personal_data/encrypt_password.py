#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a hashed password """
    encoded = password.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded, salt)

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the provided password matches the hashed password """
    encoded = password.encode()
    return bcrypt.checkpw(encoded, hashed_password)
