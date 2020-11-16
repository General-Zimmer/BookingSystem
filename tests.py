import datetime
import lagic as la
import database

res = la.reservation
isstring = la.is_string_with_space
sql = database.database()

print("Hvad vil du? "
      "1: Tilføj"
      "2: Ændrer"
      "3: Slet")
valg = int(input())

if valg == 1:
    data()
    sql.add(str(navn), str(finaldate))
    print("Reservation for", navn, "til", finaldate)
elif valg == 2:
    print("Hvem skal ændres?")
    valgnavn = input()
    sql.modify(valgnavn)
elif valg == 3:
    print("Hvem skal slettes?")
    valgnavn = input()
    sql.delete(valgnavn)
