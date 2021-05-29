
from dotenv import dotenv_values


env = dotenv_values(".env")

config = {
    "jwt": {
        "secret": env.get("JWT_SECRET"),
        "expires": int(env.get("JWT_EXPIRES", 10)),
        "iss": env.get("JWT_ISS"),
        "aud": env.get("JWT_AUD"),
        "algorithm": env.get("JWT_ALGORITHM")
    },
    "encryption": {
        "default": env.get("ENCRYPTION_DEFAULT"),
        "bcrypt": {
            "type": "bcrypt",
            "saltRounds": 10,
            "algorithm": "HS512"
        }
    }
}
