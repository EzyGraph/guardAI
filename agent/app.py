import sqlite3
from contextlib import closing


def fazer_login(usuario, senha, banco="banco_de_dados.db"):
    with closing(sqlite3.connect(banco)) as conexao:
        resultado = conexao.execute(
            "SELECT 1 FROM usuarios WHERE username = ? AND password = ? LIMIT 1",
            (usuario, senha),
        ).fetchone()

    if resultado is not None:
        return "Acesso permitido."
    return "Acesso negado!"