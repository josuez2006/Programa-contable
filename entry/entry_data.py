from dataclasses import dataclass

@dataclass(kw_only=True)
class EntryGeneral:
    date: str
    key: str
    value: str
    balance: str
    position: int
    is_negative: bool = True

    def print(self, work_sheet, letter_position: int, number_position: int) -> int:
        work_sheet[chr(letter_position) + str(number_position)] = self.date 
        work_sheet[chr(letter_position + 1) + str(number_position)] = self.key
        work_sheet[chr(letter_position + 2) + str(number_position)] = self.value
        return 1


@dataclass(kw_only=True)
class EntryBalance:
    key: str
    balance: str
    position: int


@dataclass(kw_only=True)
class EntryCommison(EntryGeneral):
    iva_key: int
    iva_value: int
    taxes_key: int
    taxes_value: int

    def print(self, work_sheet, letter_position: int, number_position: int) -> int:
        work_sheet[chr(letter_position) + str(number_position)] = self.date 
        work_sheet[chr(letter_position + 1) + str(number_position)] = self.key
        work_sheet[chr(letter_position + 2) + str(number_position)] = self.value
        work_sheet[chr(letter_position + 1) + str(number_position + 1)] = self.iva_key
        work_sheet[chr(letter_position + 2) + str(number_position + 1)] = self.iva_value

        if self.taxes_key != 'False':
            work_sheet[chr(letter_position + 1) + str(number_position + 2)] = self.taxes_key
            work_sheet[chr(letter_position + 2) + str(number_position + 2)] = self.taxes_value
            return 4

        return 3


        




@dataclass(kw_only=True)
class EntryTransfer(EntryGeneral):
    author: str

    def print(self, work_sheet, letter_position: int, number_position: int) -> int:
        work_sheet[chr(letter_position) + str(number_position)] = self.date 
        work_sheet[chr(letter_position + 1) + str(number_position)] = self.key
        work_sheet[chr(letter_position + 2) + str(number_position)] = self.value

        if self.author.isnumeric():
            work_sheet[chr(letter_position + 3) + str(number_position)] = int(self.author)
        else:
            work_sheet[chr(letter_position + 3) + str(number_position)] = self.author

        return 1



@dataclass(kw_only=True)
class EntryDebit(EntryTransfer):
    afip_number: str

    def print(self, work_sheet, letter_position: int, number_position: int) -> int:
        work_sheet[chr(letter_position) + str(number_position)] = self.date 
        work_sheet[chr(letter_position + 1) + str(number_position)] = self.key
        work_sheet[chr(letter_position + 2) + str(number_position)] = self.value

        if self.afip_number != 'False':
            work_sheet[chr(letter_position + 3) + str(number_position)] = self.afip_number

        return 1


