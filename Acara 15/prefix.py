def salam(**person):
    print(
        "Halo",
        person.get("NamaDepan", "-"),
        person.get("NamaBelakang", "-")
    )
salam(NamaDepan='Budi')
