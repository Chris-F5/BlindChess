import chess.pgn
import chess.svg
import lichess.api
import io
import os
import random

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

gameCodes = [
    "Sxov6E94",
    "CHr4jtYg",
    "Fp7E1XuI",
    "0loCLy8S",
    "FGCaM5VH",
    "OZC1cZtL",
    "5N3afPfA",
    "dyo1LC7X",
    "wMirwiJB",
    "H4H2kb6X",
    "FGCaM5VH",
    "LhucoAJY",
    "kTxChP9y",
    "TlALMGV1",
    "ooV98pbT",
    "uvoaUUUV",
    "dYPsDvIB",
    "w4LsuitG",
    "FHLp3Nqi",
    "odzWd6FL",
    "pV17qrAq",
    "Geu4jsvJ",
    "BuQ2cdJQ",
    "zDk9V3Fh",
    "CwziC6Wm",
    "hjLsSnhS",
    "RrTTKoD2",
    "iDKfl06j",
    "IVeXXG64",
    "v1W2R9U2",
    "xGZju8lI",
    "tu0Ot4CM",
    "Ox7QKTDO",
    "MPQJZcy2",
    "ytAuK5MU",
    "2VXhesjt",
    "2gdpYhHS",
    "xeKFvmFY",
    "XHnDiazo",
    "ziOefPOD",
]

print("downloading game...")

gameCodeIndex = random.randint(0, len(gameCodes) - 1)
print(gameCodeIndex)
gameCode = gameCodes[gameCodeIndex]
pgn = lichess.api.game(gameCode, format=lichess.format.PGN);


pgnStream = io.StringIO(pgn)
game = chess.pgn.read_game(pgnStream)

print("")
print("===")
print(gameCode)
print(game.headers["Event"])
print(game.headers["Date"])
print("White: " + game.headers["White"])
print("White: " + game.headers["Black"])
print("Time Control: " + game.headers["TimeControl"])
print("Variant: " + game.headers["Variant"])
print("===")
print("")

board = game.board()

def showBoard(board):
    f = open("img.svg", "w")
    f.write(chess.svg.board(board))
    f.close()
    os.system("feh --conversion-timeout 1 img.svg")

i = 2
for move in game.mainline_moves():
    print(str(i // 2) + ": " + move.uci())
    board.push(move)

    if input() != "":
        showBoard(board)
        print("the board was shown")
        input()

    i += 1
print("GAME END")
input("hit enter to show board")
showBoard(board)

