months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    date = date.capitalize()
    # If input is mm/dd/yyyy
    if "/" in date:
        try:
            mm, dd, yyyy = date.split("/")
            if (1 <= int(mm) <= 12) and (1 <= int(dd) <= 31):
                print(f"{yyyy}-{int(mm):02}-{int(dd):02}")
                break
        except:
            pass
    if "," in date:
        try:
            mm, dd, yyyy = date.split(" ")
            dd = dd.replace(",", "")
            if mm in months and (1 <= int(dd) <= 31):
                index = months.index(mm)+1
                print(f"{yyyy}-{index:02}-{int(dd):02}")
                break
        except:
            pass
