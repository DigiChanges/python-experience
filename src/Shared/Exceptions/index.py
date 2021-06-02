
from src.App.Presentation.Exceptions.ForbiddenHttpException import ForbiddenHttpException
from typing import Any
from src.App.Presentation.Exceptions.BadCredentialsHttpException import BadCredentialsHttpException
from src.App.Presentation.Exceptions.DecryptForbiddenHttpException import DecryptForbiddenHttpException
from src.App.Presentation.Exceptions.ErrorHttpException import ErrorHttpException
from src.App.Presentation.Exceptions.InvalidTokenHttpException import InvalidTokenHttpException
from src.App.Presentation.Exceptions.NotFoundHttpException import NotFoundHttpException
from src.App.Presentation.Exceptions.UserDisableHttpException import UserDisabledHttpException


def handleError(app: Any):
    BadCredentialsHttpException(app)
    DecryptForbiddenHttpException(app)
    ErrorHttpException(app)
    ForbiddenHttpException(app)
    InvalidTokenHttpException(app)
    NotFoundHttpException(app)
    UserDisabledHttpException(app)

