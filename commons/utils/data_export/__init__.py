import abc
import io
from typing import List


class DataExportService(abc.ABC):

    @abc.abstractmethod
    def export_to_stream(self, header: List[str], data: List[List]) -> io.BytesIO:
        raise NotImplemented
