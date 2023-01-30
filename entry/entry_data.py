from dataclasses import dataclass

@dataclass(kw_only=True)
class EntryGeneral:
    date: str
    key: str
    value: str
    balance: str
    position: int
    is_negative: bool = True

    def how_to_print_in_excel(self, letter_position: int, number_position: int) -> list[list]:
        self.number_of_breaks = 1
        return [
            [self.date, letter_position, number_position],
            [self.key, letter_position + 1, number_position],
            [self.value, letter_position + 2, number_position]
        ]


    def get_number_of_breaks_in_excel(self):
        return self.number_of_breaks


@dataclass(kw_only=True)
class EntryCommision(EntryGeneral):
    iva_key: int
    iva_value: int
    taxes_key: int
    taxes_value: int
    
    def how_to_print_in_excel(self, letter_position: int, number_position: int):
        if self.taxes_key == 'False':
            self.number_of_breaks = 3
            return [
                [self.date, letter_position, number_position],
                [self.key, letter_position + 1, number_position],
                [self.value, letter_position + 2, number_position],
                [self.iva_key, letter_position + 1, number_position + 1],
                [self.iva_value, letter_position + 2, number_position + 1]
            ]
        else:
            self.number_of_breaks = 4
            return [
                [self.date, letter_position, number_position],
                [self.key, letter_position + 1, number_position],
                [self.value, letter_position + 2, number_position],
                [self.iva_key, letter_position + 1, number_position + 1],
                [self.iva_value, letter_position + 2, number_position + 1],
                [self.taxes_key, letter_position + 1, number_position + 2],
                [self.taxes_value, letter_position + 2, number_position + 2]
            ]

    def get_number_of_breaks_in_excel(self):
        return self.number_of_breaks


@dataclass(kw_only=True)
class EntryTransfer(EntryGeneral):
    author: str

    def how_to_print_in_excel(self, letter_position: int, number_position: int) -> list[list]:
        self.number_of_breaks = 1
        if self.author.isnumeric():
            return [
                [self.date, letter_position, number_position],
                [self.key, letter_position + 1, number_position],
                [self.value, letter_position + 2, number_position],
                [int(self.author), letter_position + 3, number_position]
            ]
        else:
            return [
                [self.date, letter_position, number_position],
                [self.key, letter_position + 1, number_position],
                [self.value, letter_position + 2, number_position],
                [self.author, letter_position + 3, number_position]
            ]

    def get_number_of_breaks_in_excel(self):
        return self.number_of_breaks


@dataclass(kw_only=True)
class EntryDebit(EntryTransfer):
    afip_number: str

    def how_to_print_in_excel(self, letter_position: int, number_position: int):
        self.number_of_breaks = 1
        if self.afip_number == 'False':
            return [
                [self.date, letter_position, number_position],
                [self.key, letter_position + 1, number_position],
                [self.value, letter_position + 2, number_position],
                [self.author, letter_position + 3, number_position]
            ]
        else:
            return [
                [self.date, letter_position, number_position],
                [self.key, letter_position + 1, number_position],
                [self.value, letter_position + 2, number_position],
                [self.author, letter_position + 3, number_position],
                [self.afip_number, letter_position + 4, number_position],
            ] 

    def get_number_of_breaks_in_excel(self):
        return self.number_of_breaks


@dataclass(kw_only=True)
class EntryBalance:
    key: str
    balance: str
    position: int