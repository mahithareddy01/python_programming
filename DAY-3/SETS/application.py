day1=set(input("Enter attendees of day1: ").split(" "))
day2=set(input("Enter attendees of day2: ").split(" "))
day3=set(input("Enter attendees of day3: ").split(" "))
all_unique=day1|day2|day3
print(f"\nTotal unique attendees: {len(all_unique)}")
print(f"Attendees of all three days are: {day1&day2&day3}")
print(f"Attendees of exactly one day are:  {(day1-day2-day3)|(day2-day1-day3)|(day3-day1-day2)}")
print(f"Pairwise overlap counts: ")
overlap_1_2=day1&day2
overlap_2_3=day2&day3
overlap_1_3=day1&day3
print(f"Pairwise overlaps:")
print(f"Day1 & Day2 ({len(overlap_1_2)}): {sorted(overlap_1_2)}")
print(f"Day2 & Day3 ({len(overlap_2_3)}): {sorted(overlap_2_3)}")
print(f"Day1 & Day3 ({len(overlap_1_3)}): {sorted(overlap_1_3)}")