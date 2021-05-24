
from typing import Any

from fastapi import Request
from fastapi.responses import JSONResponse
from src.App.Presentation.Exceptions.DecryptForbiddenHttpException import \
    DecryptForbiddenHttpException
from src.App.Presentation.Exceptions.ErrorHttpException import \
    ErrorHttpException
from src.App.Presentation.Exceptions.NotFoundHttpException import \
    NotFoundHttpException


def handleError(app: Any):
    NotFoundHttpException(app)
    DecryptForbiddenHttpException(app)
    ErrorHttpException(app)

