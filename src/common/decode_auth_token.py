import logging
import os
from typing import Optional

import jwt
from dotenv import load_dotenv

from src.config import TEST_PUBLIC_KEY


load_dotenv()


logger = logging.getLogger(__name__)


JWT_SECRET = os.getenv("JWT_SECRET", default=TEST_PUBLIC_KEY)
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", default="RS256")


def get_user_id(token_header: Optional[str]) -> Optional[str]:
    if not token_header:
        return None

    try:
        decoded_token = jwt.decode(
            token_header,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )
    except (jwt.ExpiredSignatureError, jwt.DecodeError):
        logger.error("Invalid token or expired signature.", exc_info=True)
        return None
    return decoded_token.get("UserId")


def get_user_roles(token_header: Optional[str]) -> Optional[str]:
    if not token_header:
        return None

    try:
        decoded_token = jwt.decode(
            token_header,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )
    except (jwt.ExpiredSignatureError, jwt.DecodeError):
        logger.error("Invalid token or expired signature.", exc_info=True)
        return None
    return decoded_token.get("Roles")
