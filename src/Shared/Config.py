
from dotenv import dotenv_values


env = dotenv_values(".env")

config = {
    "jwt": {
        "secret": env.get("JWT_SECRET"),
        "expires": env.get("JWT_EXPIRES"),
        "iss": env.get("JWT_ISS"),
        "aud": env.get("JWT_AUD"),
        "algorithm": env.get("JWT_ALGORITHM")
    }
}