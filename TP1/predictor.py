aminoacid_structure_preferences = {
    "A": {
        "name": "Alanine",
        "a_helix": 1.41,
        "b_sheet": 0.72,
        "loop": 0.82,
    },
    "C": {
        "name": "Cysteine",
        "a_helix": 0.66,
        "b_sheet": 1.4,
        "loop": 0.54,
    },
    "D": {
        "name": "Aspartic Acid",
        "a_helix": 0.99,
        "b_sheet": 0.39,
        "loop": 1.24,
    },
    "E": {
        "name": "Glutamic Acid",
        "a_helix": 1.59,
        "b_sheet": 0.52,
        "loop": 1.01,
    },
    "F": {
        "name": "Phenylalanine",
        "a_helix": 1.16,
        "b_sheet": 1.33,
        "loop": 0.59,
    },
    "G": {
        "name": "Glycine",
        "a_helix": 0.43,
        "b_sheet": 0.58,
        "loop": 1.77,
    },
    "H": {
        "name": "Histidine",
        "a_helix": 1.05,
        "b_sheet": 0.80,
        "loop": 0.81,
    },
    "I": {
        "name": "Isoleucine",
        "a_helix": 1.09,
        "b_sheet": 1.67,
        "loop": 0.47,
    },
    "L": {
        "name": "Leucine",
        "a_helix": 1.34,
        "b_sheet": 1.22,
        "loop": 0.57,
    },
    "K": {
        "name": "Lysine",
        "a_helix": 1.23,
        "b_sheet": 0.69,
        "loop": 1.07,
    },
    "M": {
        "name": "Methionine",
        "a_helix": 1.3,
        "b_sheet": 1.14,
        "loop": 0.52,
    },
    "N": {
        "name": "Asparagine",
        "a_helix": 0.76,
        "b_sheet": 0.48,
        "loop": 1.34,
    },
    "P": {
        "name": "Proline",
        "a_helix": 0.34,
        "b_sheet": 0.31,
        "loop": 1.32,
    },
    "Q": {
        "name": "Glutamine",
        "a_helix": 1.27,
        "b_sheet": 0.98,
        "loop": 0.84,
    },
    "R": {
        "name": "Arginine",
        "a_helix": 1.21,
        "b_sheet": 0.84,
        "loop": 0.9,
    },
    "S": {
        "name": "Serine",
        "a_helix": 0.57,
        "b_sheet": 0.96,
        "loop": 1.22,
    },
    "T": {
        "name": "Threonine",
        "a_helix": 0.76,
        "b_sheet": 1.17,
        "loop": 0.9,
    },
    "V": {
        "name": "Valine",
        "a_helix": 0.9,
        "b_sheet": 1.87,
        "loop": 0.41,
    },
    "W": {
        "name": "Tryptophan",
        "a_helix": 1.02,
        "b_sheet": 1.35,
        "loop": 0.65,
    },
    "Y": {
        "name": "Tyrosine",
        "a_helix": 0.74,
        "b_sheet": 1.45,
        "loop": 0.76,
    },
}


def predict_secondary_structure(protein_sequence: str) -> str:
    prediction = []
    for aminoacid in protein_sequence:
        preference = aminoacid_structure_preferences[aminoacid]
        preferred_structure_probability = max(
            preference["a_helix"],
            preference["b_sheet"],
            preference["loop"],
        )

        if preferred_structure_probability == preference["a_helix"]:
            prediction.append("H")
        elif preferred_structure_probability == preference["b_sheet"]:
            prediction.append("B")
        else:
            prediction.append("L")

    return "".join(prediction)


if __name__ == "__main__":
    """
    Example in bash:
    >>>  python predictor.py "CGTAACAAGGTTTCCGTAGGTGAACC"
    protein_sequence='CGTAACAAGGTTTCCGTAGGTGAACC'
    prediction='BLBHHBHHLLBBBBBLBHLLBLHHBB'
    """
    import sys

    script_name = sys.argv[0]
    protein_sequence = sys.argv[1]
    print(f"{protein_sequence=}")
    prediction = predict_secondary_structure(protein_sequence)
    print(f"{prediction=}")
