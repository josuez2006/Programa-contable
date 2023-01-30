from entry.entry_data import EntryGeneral


def order_positions(entries: list) -> list:
    positions = []
    for entry in entries:
        positions.append(entry.position)

    positions.sort()
    return positions

def equal_position(entries: list, position) -> EntryGeneral:
    # for entry in entries:
    #     if entry.position == position:
    #         print(entry)
    #         return entry
    return [entry for entry in entries if entry.position == position]

def match_entries(sorted_entries: list, all_entries: list) -> None:
    entries_positions: list = order_positions(all_entries)
    # print(entries_positions)

    for i in range(1, len(sorted_entries) - 1, 2):
        previous_entry = equal_position(all_entries, entries_positions[i-1])
        current_entry = equal_position(sorted_entries, entries_positions[i])

        # print(entries_positions[i-1])
        # print(entries_positions[i])
        # print(previous_entry[i])
        # print(current_entry[i])
        
        if current_entry != [] and current_entry != None:
            if current_entry.balance > previous_entry.balance:
                current_entry.is_negative = True
        