import os

def parse_racks(input_lines):
    racks = []
    current_rack = -1

    for line in input_lines:
        if line.startswith("#"):
            current_rack += 1
            racks.append([])
        else:
            racks[current_rack].append(line.strip())

    return racks

def parse_lists(input_lines):
    lists = []
    current_list = []

    for line in input_lines:
        if line.strip() == "":
            if current_list:
                lists.append(current_list)
                current_list = []
        else:
            current_list.append(line.strip())
    
    if current_list:
        lists.append(current_list)
    
    return lists

def optimize_lists(racks, lists):
    optimized_lists = []

    for shopping_list in lists:
        optimized_list = []
        remaining_items = []

        for item in shopping_list:
            found = False
            for rack_num, rack in enumerate(racks):
                for rack_item in rack:
                    if rack_item.lower() == item.lower():
                        optimized_list.append((item, rack_item, rack_num))
                        found = True
                        break
                if found:
                    break
            
            if not found:
                for rack_num, rack in enumerate(racks):
                    for rack_item in rack:
                        if item.lower() in rack_item.lower():
                            optimized_list.append((item, rack_item, rack_num))
                            found = True
                            break
                    if found:
                        break
            
            if not found:
                remaining_items.append((item, item, None))
        
        optimized_list.extend(remaining_items)
        optimized_list.sort(key=lambda x: (x[2] is None, x[2]))
        optimized_lists.append(optimized_list)
    
    return optimized_lists

def print_optimized_lists(optimized_lists):
    for i, optimized_list in enumerate(optimized_lists):
        print(f"Seznam {i + 1}:")
        for j, (original_name, new_name, rack_number) in enumerate(optimized_list):
            if rack_number is None:
                print(f"{j}. {original_name} -> N/A")
            else:
                print(f"{j}. {original_name} -> #{rack_number} {new_name}")
        print()

def main():
    test_dir = "./test/uloha6/"
    for test_num in range(3):
        print(f"Test {test_num}:")

        with open(os.path.join(test_dir, f"000{test_num}_in.txt"), "r", encoding="utf-8") as f:
            input_data = f.read().strip()

        input_sections = input_data.split("\n\n")
        if len(input_sections) < 2:
            print("Neplatny vstup\n")
            continue

        racks = parse_racks(input_sections[0].split("\n"))
        lists = parse_lists(input_sections[1:])
        
        optimized_lists = optimize_lists(racks, lists)
        print_optimized_lists(optimized_lists)

if __name__ == "__main__":
    main()