from entry.entry_data import EntryGeneral


def order_positions(entries: list) -> list:
    positions = []
    for entry in entries:
        positions.append(entry.position)

    positions.sort()
    return positions


def equal_position(entries: list, position) -> EntryGeneral:
    return [entry for entry in entries if entry.position == position]


def match_entries(sorted_entries: list, all_entries: list) -> None:
    entries_positions: list = order_positions(all_entries)

    for i in range(1, len(entries_positions) - 1):
        previous_entry = equal_position(all_entries, entries_positions[i-1])
        current_entry = equal_position(sorted_entries, entries_positions[i])
        
        if current_entry != [] and current_entry != None:
            if current_entry[0].balance > previous_entry[0].balance:
                current_entry[0].is_negative = False

    
        