from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()
api_app = FastAPI()

data = {
    "antonowka": {
        "Kwaśność/Słodkość": 4.00,
        "Chrupkość/Miękkość Miąższu": 6.00,
        "Opis skórki": "Skórka gładka, błyszcząca",
        "Opis miąższu": "Miąższ jasny, soczysty",
    },
    "reneta_szara": {
        "Kwaśność/Słodkość": 2.00,
        "Chrupkość/Miękkość Miąższu": 7.00,
        "Opis skórki": "Skórka pokryta szarawym, chropowatym nalotem",
        "Opis miąższu": "Miąższ winny, o korzennym aromacie",
    },
    "lobo": {
        "Kwaśność/Słodkość": 5.50,
        "Chrupkość/Miękkość Miąższu": 7.50,
        "Opis skórki": "Skórka gładka, błyszcząca",
        "Opis miąższu": "Miąższ zielonkawokremowy, kruchy, bardzo soczysty",
    },
    "ligol": {
        "Kwaśność/Słodkość": 8.00,
        "Chrupkość/Miękkość Miąższu": 2.00,
        "Opis skórki": "Skórka mocna, gładka i błyszcząca",
        "Opis miąższu": "Miąższ kremowy, soczysty, jędrny, aromatyczny",
    },
    "golden_delicious": {
        "Kwaśność/Słodkość": 7.00,
        "Chrupkość/Miękkość Miąższu": 4.00,
        "Opis skórki": "Skórka lekko błyszcząca, zielonkawożółta lub żółta",
        "Opis miąższu": "Miąższ soczysty, kruchy, winno-słodki",
    },
    "gala": {
        "Kwaśność/Słodkość": 9.00,
        "Chrupkość/Miękkość Miąższu": 2.50,
        "Opis skórki": "Żebrowanie przy kielichu, skórka pokryta marmurkowym rumieńcem",
        "Opis miąższu": "Miąższ kremowożółty, soczysty, chrupki",
    },
    "idared": {
        "Kwaśność/Słodkość": 3.00,
        "Chrupkość/Miękkość Miąższu": 5.00,
        "Opis skórki": " Skórka mocna, gruba i błyszcząca",
        "Opis miąższu": "Miąższ biały, lekko kremowy, drobnoziarnisty, soczysty",
    },
    "papierowka": {
        "Kwaśność/Słodkość": 3.00,
        "Chrupkość/Miękkość Miąższu": 9.00,
        "Opis skórki": "Skórka cienka, gładka, sucha",
        "Opis miąższu": "Miąższ bardzo delikatny, zielonkawobiały",
    },
    "gloster": {
        "Kwaśność/Słodkość": 4.00,
        "Chrupkość/Miękkość Miąższu": 3.00,
        "Opis skórki": "Skórka lekko błyszcząca, zielonkawożółta z rozległym rumieńcem",
        "Opis miąższu": "Miąższ średnioziarnisty, kruchy, białokremowy",
    },
    "jonagold": {
        "Kwaśność/Słodkość": 5.50,
        "Chrupkość/Miękkość Miąższu": 6.00,
        "Opis skórki": "Skórka średniej grubości",
        "Opis miąższu": "Miąższ żółty, gruboziarnisty, ścisły, soczysty",
    },
    "szampion": {
        "Kwaśność/Słodkość": 7.00,
        "Chrupkość/Miękkość Miąższu": 7.00,
        "Opis skórki": "Skórka gładka, zielonkawożółta, pokryta rozmyto-paskowanym rumieńcem",
        "Opis miąższu": "Miąższ soczysty, aromatyczny",
    },
    "granny_zielone": {
        "Kwaśność/Słodkość": 7.00,
        "Chrupkość/Miękkość Miąższu": 4.5,
        "Opis skórki": "Skórka gładka, tłustawa i lśniąca",
        "Opis miąższu": "Miąższ zielonkawobiały, soczysty i jędrny",
    },
    "cortland": {
        "Kwaśność/Słodkość": 6.00,
        "Chrupkość/Miękkość Miąższu": 6.00,
        "Opis skórki": "Skórka cienka, o karminowym rumieńcu",
        "Opis miąższu": " Miąższ biały, drobnoziarnisty, kruchy",
    },
    "jonatan": {
        "Kwaśność/Słodkość": 7.00,
        "Chrupkość/Miękkość Miąższu": 4.00,
        "Opis skórki": "Skórka mocna, błyszcząca, ze smużkowatym rumieńcem",
        "Opis miąższu": "Miąższ kremowo-biały, aromatyczny, ścisły",
    },
    "red_prince": {
        "Kwaśność/Słodkość": 5.50,
        "Chrupkość/Miękkość Miąższu": 6.00,
        "Opis skórki": "Skórka błyszcząca, mocna, w 95% pokryta bordowym rumieńcem",
        "Opis miąższu": "Miąższ kremowożółty, ścisły i twardy",
    },
    "red_delicious": {
        "Kwaśność/Słodkość": 7.00,
        "Chrupkość/Miękkość Miąższu": 4.00,
        "Opis skórki": "Skórka intensywnie bordowa, błyszcząca",
        "Opis miąższu": "Miąższ chrupiący, soczysty",
    },
    "alwa": {
        "Kwaśność/Słodkość": 4.00,
        "Chrupkość/Miękkość Miąższu": 4.50,
        "Opis skórki": "Skórka zielonkawożółta z dużym czerwonym rumieńcem",
        "Opis miąższu": "Miąższ chrupki, soczysty",
    },
    "elize": {
        "Kwaśność/Słodkość": 7.00,
        "Chrupkość/Miękkość Miąższu": 3.00,
        "Opis skórki": "Skórka gładka, sucha",
        "Opis miąższu": "Miąższ białozielony, soczysty, aromatyczny",
    },
    "pinova": {
        "Kwaśność/Słodkość": 5.00,
        "Chrupkość/Miękkość Miąższu": 2.50,
        "Opis skórki": "Skórka sucha, zielonożółta, ok. 75% rumieńca",
        "Opis miąższu": "Miąższ średnio zwarty, żółtawy",
    },
}

@api_app.get("/apples/{name}")
async def get_apple_by_name(name: str):
    return data.get(name.lower(), HTTPException(status_code=404, detail="Apple not found, try without polish letters"))

@api_app.get("/apples")
async def get_apples():
    return data


app.mount('/api', api_app)
app.mount("/", StaticFiles(directory="static", html=True), name="static")