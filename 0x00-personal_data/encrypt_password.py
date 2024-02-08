#!/usr/bin/env python3
"""
Encrypt password
"""
import bcrypt


def hash_password(password):
    """returns a hashed password"""
    encoded = password.encode()
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(encoded, salt)
    return hashed_password


def is_valid(hashed_password, password):
    """Checks if the password is correct"""
    return bcrypt.checkpw(password.encode(), hashed_password)
