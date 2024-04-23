class Film:
    def __init__(self, judul, rilis, director):
        self.judul = judul
        self.rilis = rilis
        self.director = director

films = [
    Film("Ballerina", 2023, "Lee Chung-hyun"),
    Film("Howl's Moving Castle", 2004, "Hayao Miyazaki"),
    Film("Kingdom", 2019, "Kim Seong=hun"),
    Film("Midnight", 2021, "Kwon Oh-seung"),
    Film("The Call", 2020, "Lee Chung-hyun")
]

print("-----Elkom 2-----")

for i, film in enumerate(films, start=1):
    print(f"Film favorit ke-{i}:")
    print(f"Judul: {film.judul}")
    print(f"Rilis: {film.rilis}")
    print(f"Director: {film.director}")
    if i < len(films):
        print("=" * 20)
