from entry.entry_data import *


def test_entry_general():
    entry = EntryGeneral('11-01', 'SERVICIO ACREDITAMIENTO DE HABERS', 5540.03, 15000.5, 5000)
    entry.how_to_print_in_excel()

    