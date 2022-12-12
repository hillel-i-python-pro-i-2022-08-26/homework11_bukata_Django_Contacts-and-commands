import logging
from typing import ClassVar
from collections.abc import Callable

from django.http import HttpRequest

from apps.middleware.models import Request


class RequestInfoMiddleware:
    # its django method which will be given to ass and its use for django settings (Callable)
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        # we take logger from django
        self.logger = logging.getLogger("django")
        # and leave here log message
        self.logger.info("here")

    def __call__(self, request: HttpRequest):
        # user session start
        session = request.session

        if not session.session_key:
            session.save()
        session_key = session.session_key
        # user session stop

        visit = Request.objects.filter(
            user=request.user_id, session_key=session_key, path=request.path
        ).first()
        if visit is None:
            visit = Request.objects(request.user_id, request.path, session_key)
            message = f"Info on request: {visit}"
            self.logger.info(f"[start: ] {message}")
        visit = visit.count() + 1
        visit.save()

        response = self.get_response(request)
        self.logger.info(f"[finish:] {message}")

        return response


class SimpleLoggingMiddleware:
    _NAME: ClassVar[str] = "first"
    # its django method which will be given to ass and its use for django settings (Callable)
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        # we take logger from django
        self.logger = logging.getLogger("django")
        # and leave here log message
        self.logger.info(f"init {self._NAME}")

    def __call__(self, request: HttpRequest):
        session = request.session
        session_key = session.session_key
        if not session.session_key:
            session.save()
        session_key = session.session_key

        # here we awake the message with info about request and user, request.user id isuer name
        message = f"{self._NAME} {request.path} {request.user.is_authenticated} {request.user} {session_key}"
        self.logger.info(f"[before] {message}")
        response = self.get_response(request)
        self.logger.info(f"[after] {message}")
        return response


class SimpleLoggingMiddleware2(SimpleLoggingMiddleware):
    _NAME: ClassVar[str] = "second"
