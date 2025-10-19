votes = [input() for _ in range(9)]
if votes.count("Tiger") > votes.count("Lion"):
    print("Tiger")
else:
    print("Lion")