from fastapi import HTTPException, status


class DefaultException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(DefaultException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь уже существует"


class IncorrectEmailOrPasswordException(DefaultException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверная почта или пароль"


class TokenExpiredException(DefaultException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Срок действия токена истек"


class TokenAbsentException(DefaultException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"


class IncorrectTokenFormatException(DefaultException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неверный формат токена"


class UserIsNotPresentException(DefaultException):
    status_code=status.HTTP_401_UNAUTHORIZED


class CannotProcessCSV(DefaultException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось обработать CSV файл"


class CannotAddDataToDatabase(DefaultException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось добавить запись"


class FileNotFound(DefaultException):
    status_code=status.HTTP_404_NOT_FOUND
    detail="Файл не найден"
