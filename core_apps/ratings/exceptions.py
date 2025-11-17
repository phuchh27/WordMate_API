from rest_framework.exceptions import APIException


class YouhaveAlreadyRated(APIException):
    status_code = 400
    default_detail = "You have already rated this article."
    default_code = "you_have_already_rated"
