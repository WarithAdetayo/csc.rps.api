from commons.utils.data_export.simple_csv_export import SimpleCSVExportService


class ExportHandler:

    _export_services = [
        SimpleCSVExportService()
    ]

    _default = 0

    @classmethod
    def get_export_service(cls):
        return cls._export_services[cls._default]
