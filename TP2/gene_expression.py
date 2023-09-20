QUIT = "SALIR".casefold()

START_CODON = "AUG"

STOP_CODONS = [
    "UAA",
    "UAG",
    "UGA",
]

THYMINE = "T"

BASES = {
    "U": "A",
    "C": "G",
    "A": "U",
    "G": "C",
}


def pair(arnm: str) -> list[tuple[str, str]]:
    proteine: list[tuple[str, str]] = []

    for i in range(0, len(arnm), 3):
        codon = arnm[i : i + 3]
        computed_anticodon = "".join([BASES.get(base, "") for base in codon])

        tries = 3
        while tries > 0:
            anticodon = (
                input(f"Traducción: ingresa el codón complementario para {codon}: ")
                .strip()
                .upper()
            )
            if computed_anticodon == anticodon:
                proteine.append((codon, anticodon))
                break
            else:
                tries -= 1
                print(f"El complemento no es válido. Intentos restantes: {tries}")

    return proteine


INSTRUCTIONS = f"""
Bienvenido al juego de expressión génica!

Tu objetivo es sintetizar proteínas y para ellos tendrás que ingresar una
cadena de ARN mensajero (ARNm) y luego ingresar uno a uno los aminoácidos
correspondientes al ARN de transferencia (ARNt) para obtener una proteína.

Si ingresás un ARNm inválido, perdés 1 punto.
Además, tenés 3 intentos para poder aparear un codón de ARNm con un codón de ARNt,
si fallás perdés 5 puntos. En cambio, si lográs sintetizar la proteína
ganás 20 puntos más la proteína.

¡Buena suerte!

PISTA: Ingresa {QUIT} para salir.
"""


def main() -> None:
    print(INSTRUCTIONS)

    score = 0

    while True:
        print()
        print(f"~~~~~ Puntos: {score} ~~~~~")
        print()

        player_input = (
            input("Transcripción: ingresa una cadena de ARNm: ").strip().upper()
        )

        if player_input.casefold() == QUIT:
            print("¡Gracias por jugar!")
            break

        if (
            not player_input
            or not player_input.startswith(START_CODON)
            or not player_input.endswith(tuple(STOP_CODONS))
            or THYMINE in player_input
            or len(player_input) % 3 != 0
        ):
            print(
                "Traducción interrumpida: "
                "¡No puedo unirme al ribosoma, tu gen es mutante!"
            )
            score -= 1
            continue

        arnm = player_input

        try:
            proteine = pair(arnm)
            print(f"¡Felicitaciones! Obtuviste la proteína: {proteine}")
            score += 20
        except Exception:
            print("¡No tenés suficientes nutrientes para sintetizar proteínas!")
            score -= 5


if __name__ == "__main__":
    main()
