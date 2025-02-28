import io
from typing import List

from commons.utils.data_export import DataExportService


class SimpleCSVExportService(DataExportService):

    def export_to_stream(self, header: List[str], data: List[List]) -> io.BytesIO:
        csv_data = ','.join(header)
        for row in data:
            csv_data += '\n' + ','.join([f'"{str(r)}"' for r in row])

        buffer = io.BytesIO()
        buffer.write(csv_data.encode())

        return buffer
