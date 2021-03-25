import typing
from datetime import datetime
import itertools


class Date:
    _date_string: str = ''
    _datetime: typing.Union[datetime, None] = datetime

    def set(self, date_string: str):
        self._date_string = date_string.strip()
        formats = [
            "%Y-%m-%d %H:%M %Z",
            "%Y-%m-%d %H:%M:%S %Z",
            "%Y-%m-%d %H %Z",
            "%Y-%m-%d %Z",
            "%Y-%m %Z",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H",
            "%Y-%m-%d",
            "%Y-%m"

        ]
        for _format in formats:
            try:
                self._datetime = datetime.strptime(self._date_string, _format)
                break
            except ValueError:
                self._datetime = None
        if self._datetime is None:
            raise ValueError(f"Could not parse date format! \"{date_string}\"")

    @staticmethod
    def fromtimestamp_str(value: str) -> datetime:
        return datetime.fromtimestamp(int(value))

    def get(self) -> datetime:
        return self._datetime
