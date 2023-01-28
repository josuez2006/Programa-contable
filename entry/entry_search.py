import re
from abc import ABC, abstractmethod

from entry.resources import for_each_item_do, disarray
from entry.entry_data import *
from entry.entry_is_negative import *


class EntrySearcher(ABC):
    @abstractmethod
    def search(self, text: str) -> None:
        pass



class EntryGeneralSearcher(EntrySearcher):
    text: str
    pattern: str
    keys: list


    def __init__(self, keys):
        self.pattern = "[a-zA-Z\s\.\,]+[0-9]+\n[0-9\,\.]+\n"
        self.keys = keys


    def search(self, text: str) -> None:
        self.text = text
        positions = self.find_entries_position(self.keys)
        positions = disarray(positions)
        entries = self.find_entries_data(positions)
        entries = self.modify_entries_format(entries)

        return self.create_entries(entries)


    def find_entries_position(self, keys: list) -> list:
        return for_each_item_do(keys, self.find_entry_position)


    def find_entries_data(self, positions) -> list:
        return for_each_item_do(positions, self.find_entry_data)
        

    def modify_entries_format(self, entries: list) -> list:
        return for_each_item_do(entries, self.modify_entry_format)


    def create_entries(self, entries: list) -> list:
        return for_each_item_do(entries, self.create_entry)



    def find_entry_position(self, key: str) -> list:
        return [i for i in range(len(self.text)) if self.text.startswith(key, i)]


    def find_entry_data(self, start_positon: int) -> str:
        # Include date of the entry
        start_entry_position = start_positon - 6

        # Cut the text from the start entry position
        entry = self.text[start_entry_position:]

        # Use a pattern to determine the end of the entry
        end_entry_position = re.search(self.pattern , entry).end()

        # Cut the text to the end of the entry position
        entry = entry[:end_entry_position]

        entry = entry + '\n' + str(start_positon)

        return entry


    def modify_entry_format(self, entry: str) -> list:
        new_entry = []
        for element in entry.split('\n'):
            if element != ' ' and element != '':
                new_entry.append(element)

        return new_entry


    def create_entry(self, entry:list) -> EntryGeneral:
        return EntryGeneral(date = entry[0], key = entry[1], value = entry[2], balance = entry[3], position = int(entry[4]))



class EntryTransferSearcher(EntrySearcher):
    text: str
    pattern: str
    keys: list
    validated_entry: bool


    def __init__(self, keys):
        self.pattern = "[0-9]+\n[0-9\s\.\,]+\n[a-zA-Z\s\,]+[^0-9]"
        self.keys = keys
        self.validated_entry = True


    def search(self, text: str) -> None:
        self.text = text
        positions = self.find_entries_position(self.keys)
        positions = disarray(positions)
        entries = self.find_entries_data(positions)
        entries = self.modify_entries_format(entries)

        entries = self.create_entries(entries)

        # delete the transfer of American express
        entries = self.validate_entries(entries)

        self.make_positions_int(entries)

        return entries


    def find_entries_position(self, keys: list) -> list:
        return for_each_item_do(keys, self.find_entry_position)


    def find_entries_data(self, positions) -> list:
        return for_each_item_do(positions, self.find_entry_data)
        

    def modify_entries_format(self, entries: list) -> list:
        return for_each_item_do(entries, self.modify_entry_format)


    def create_entries(self, entries: list) -> list:
        return for_each_item_do(entries, self.create_entry)

    
    def validate_entries(self, entries: list) -> list:
        return [entry for entry in entries if entry.author != 'AMERICAN EXPRESS' and not entry.author.isalpha()]


    def make_positions_int(self, entries: list) -> list:
        for entry in entries:
            entry.position = int(entry.position)

    def find_entry_position(self, key: str) -> list:
        return [i for i in range(len(self.text)) if self.text.startswith(key, i)]


    def find_entry_data(self, start_positon: int) -> str:
        # Include date of the entry
        start_entry_position = start_positon - 6

        # Cut the text from the start entry position
        entry = self.text[start_entry_position:]

        # Use a pattern to determine the end of the entry
        end_entry_position = re.search(self.pattern , entry).end()

        # Cut the text to the end of the entry position
        entry = entry[:end_entry_position]

        entry = entry + '\n' + str(start_positon)

        return entry
    

    def modify_entry_format(self, entry: str) -> list:
        newEntry = []
        for element in entry.split('\n'):
            if element != ' ' and element != '':
                newEntry.append(element)

        return newEntry


    def create_entry(self, entry: list) -> EntryTransfer:
        if len(entry) > 6:
            return EntryTransfer(date = entry[0], key = entry[1], value = entry[2], balance = entry[3], author = entry[4], position = entry[6])
        else:
            return EntryTransfer(date = entry[0], key = entry[1], value = entry[2], balance = entry[3], author = entry[4], position = int(entry[5]))



class EntryDebitSearcher(EntrySearcher):
    text: str
    pattern: str
    keys: list
    validated_entry: bool


    def __init__(self, keys):
        self.pattern = "[0-9]+\n[0-9\s\.\,]+\n[a-zA-Z\,\s]+"
        self.keys = keys
        self.validated_entry = True


    def search(self, text: str) -> None:
        self.text = text
        positions = self.find_entries_position(self.keys)
        positions = disarray(positions)
        entries = self.find_entries_data(positions)
        entries = self.modify_entries_format(entries)

        entries = self.create_entries(entries)


        return entries


    def find_entries_position(self, keys: list) -> list:
        return for_each_item_do(keys, self.find_entry_position)


    def find_entries_data(self, positions) -> list:
        return for_each_item_do(positions, self.find_entry_data)
        

    def modify_entries_format(self, entries: list) -> list:
        return for_each_item_do(entries, self.modify_entry_format)


    def create_entries(self, entries: list) -> list:
        return for_each_item_do(entries, self.create_entry)



    def find_entry_position(self, key: str) -> list:
        return [i for i in range(len(self.text)) if self.text.startswith(key, i)]


    def find_entry_data(self, start_positon: int) -> str:
        # Include date of the entry
        start_entry_position = start_positon - 6

        # Cut the text from the start entry position
        start_entry = self.text[start_entry_position:]


        end_entry_position = re.search(self.pattern , start_entry).end()

        # Cut the text to the end of the entry position
        entry = start_entry[:end_entry_position]

        entry = entry + '\n' + str(start_positon)

        if entry.find('AFIP') != -1:
            
            self.pattern = "[0-9]+\n[0-9\s\.\,]+\n[a-zA-Z\s\,]+[^0-9]"
            afip_number = self.find_afip_data(start_entry)
            entry = entry + '\n' + afip_number

            return entry

        entry = entry +  '\n' + 'False'


        return entry
    

    def find_afip_data(self, text: str) -> str:
        pattern = '[A-Z]{1}[0-9]+[A-Z]{1}[0-9]+'
        start_position = re.search(pattern, text).start()
        end_position = re.search(pattern, text).end()
        new_text = text[start_position:end_position]
        return new_text



    def modify_entry_format(self, entry: str) -> list:
        newEntry = []
        for element in entry.split('\n'):
            if element != ' ' and element != '':
                newEntry.append(element)

        return newEntry


    def create_entry(self, entry: list) -> EntryTransfer:
        return EntryDebit(date = entry[0], key = entry[1], value = entry[2], balance = entry[3], author = entry[4], position = int(entry[6]), afip_number = entry[7])



class EntryCommisionSearcher(EntrySearcher):
    text: str
    pattern: str
    keys: list


    def __init__(self, keys):
        self.pattern = "[a-zA-Z\s\.\,]+[0-9s\.\,]+\n[0-9s\.\,]+"
        self.keys = keys


    def search(self, text: str) -> None:
        self.text = text
        positions = self.find_entries_position(self.keys)
        positions = disarray(positions)
        entries = self.find_entries_data(positions)
        entries = self.modify_entries_format(entries)

        return self.create_entries(entries)


    def find_entries_position(self, keys: list) -> list:
        return for_each_item_do(keys, self.find_entry_position)


    def find_entries_data(self, positions) -> list:
        return for_each_item_do(positions, self.find_entry_data)
        

    def modify_entries_format(self, entries: list) -> list:
        return for_each_item_do(entries, self.modify_entry_format)


    def create_entries(self, entries: list) -> list:
        return for_each_item_do(entries, self.create_entry)



    def find_entry_position(self, key: str) -> list:
        return [i for i in range(len(self.text)) if self.text.startswith(key, i)]


    def find_entry_data(self, start_positon) -> str:
        # Include date of the entry
        start_entry_position = start_positon - 6

        # Cut the text from the start entry position
        entry = self.text[start_entry_position:]

        # Use a pattern to determine the end of the entry
        end_entry_position = re.search(self.pattern , entry).end()

        # Cut the text to the end of the entry position
        entry = entry[:end_entry_position]

        entry = entry + '\n' + str(start_positon)

        iva_and_taxes = self.find_missing_data(start_positon)

        return entry + '\n' + iva_and_taxes


    

    def modify_entry_format(self, entry: str) -> list:
        newEntry = []
        for element in entry.split('\n'):
            if element != ' ' and element != '':
                newEntry.append(element)

        return newEntry


    def create_entry(self, entry:list) -> EntryGeneral:
        return EntryCommison(date = entry[0], key = entry[1], value = entry[2], balance = entry[3], position = int(entry[4]), iva_key = entry[5], iva_value = entry[6], taxes_key = entry[7], taxes_value = entry[8])


    def find_missing_data(self, start_position: int):
        # Select the text from the entry start
        new_text = self.text[start_position:]

        # Define a pattern to find iva and taxes
        pattern = '[a-zA-Z\s\.]+[0-9\,]+\n'
        iva = self.find_iva(new_text, pattern)
        taxes = self.find_taxes(new_text, pattern)

        # In the case that taxes are not found return false
        if taxes == False:
            return iva + 'False\nFalse'
        else:
            return iva + taxes


    def find_iva(self, text: str, pattern: str):
        start_position = text.find('IVA')
        new_text = text[start_position:]
        end_position = re.search(pattern, new_text).end()
        return new_text[:end_position]

    def find_taxes(self, text: str, pattern: str):
        start_position = text.find('IMP. ING. BRUTOS')

        # Check if taxes belongs to the current entry
        for key in self.keys:
            # Find the next commison entry
            checker = text[10:].find(key)
            # Test if the taxes found belongs to another commison entry
            if checker < start_position and checker != -1:
                return False
        

        new_text = text[start_position:]
        end_position = re.search(pattern, new_text).end()
        return new_text[:end_position]


class EntryBalanceSearcher(EntrySearcher):
    text: str
    pattern: str
    keys: list


    def __init__(self, keys):
        self.pattern = "[a-zA-Z\s\.\,]+[0-9\.\,]+"
        self.keys = keys


    def search(self, text: str) -> None:
        self.text = text
        positions = self.find_entries_position(self.keys)
        positions = disarray(positions)
        entries = self.find_entries_data(positions)
        entries = self.modify_entries_format(entries)

        return self.create_entries(entries)


    def find_entries_position(self, keys: list) -> list:
        return for_each_item_do(keys, self.find_entry_position)


    def find_entries_data(self, positions) -> list:
        return for_each_item_do(positions, self.find_entry_data)
        

    def modify_entries_format(self, entries: list) -> list:
        return for_each_item_do(entries, self.modify_entry_format)


    def create_entries(self, entries: list) -> list:
        return for_each_item_do(entries, self.create_entry)



    def find_entry_position(self, key: str) -> list:
        return [i for i in range(len(self.text)) if self.text.startswith(key, i)]


    def find_entry_data(self, start_positon: int) -> str:
        start_entry_position = start_positon

        # Cut the text from the start entry position
        entry = self.text[start_entry_position:]

        # Use a pattern to determine the end of the entry
        end_entry_position = re.search(self.pattern , entry).end()

        # Cut the text to the end of the entry position
        entry = entry[:end_entry_position]

        entry = entry + '\n' + str(start_positon)

        return entry


    def modify_entry_format(self, entry: str) -> list:
        new_entry = []
        for element in entry.split('\n'):
            if element != ' ' and element != '':
                new_entry.append(element)

        return new_entry


    def create_entry(self, entry:list) -> EntryGeneral:
        return EntryBalance(key = entry[0], balance = entry[1], position = int(entry[2]))



def search_entries(text):
    searchers = [
        EntryGeneralSearcher(['PAGO VISA EMPRESA', 'SERVICIO', 'ECHEQ']),
        EntryTransferSearcher(['TRF', 'TRANS']),
        EntryDebitSearcher(['DEB. AUTOM. DE SERV.']),
        EntryCommisionSearcher(['COM.', 'COMISION'])
    ]

    entries_found = []

    for searcher in searchers:
        entries_found.append(searcher.search(text))


    entries_found = disarray(entries_found)

    return entries_found


def search_all_entries(text):
    searchers = [
        EntryBalanceSearcher(['SALDO INICIAL' ,'SALDO ANTERIOR']),
        EntryGeneralSearcher(['PAGO VISA EMPRESA', 'SERVICIO', 'ECHEQ']),
        EntryGeneralSearcher(['ACREDITAMIENTOS PRISMA - COMERCIOS', 'ING. BRUTOS S/ CRED']),
        EntryTransferSearcher(['TRF', 'TRANS']),
        EntryDebitSearcher(['DEB. AUTOM. DE SERV.']),
        EntryCommisionSearcher(['COM.', 'COMISION'])
    ]

    entries_found = []

    for searcher in searchers:
        entries_found.append(searcher.search(text))


    entries_found = disarray(entries_found)

    return entries_found


def get_entries(text: str) -> list:
    sorted_entries = search_entries(text)
    all_entries = search_all_entries(text)
    all_entries_positions = order_positions(all_entries)
    match_entries(sorted_entries, all_entries, all_entries_positions)
    return sorted_entries