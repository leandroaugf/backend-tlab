def test_adicionar_usuario_success(client):
    resposta = client.post(
        "/AdicionarUsuario/",
        params={"email": "teste@gmail.com", "nome": "Teste"},
    )

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["email"] == "teste@gmail.com"
    assert corpo["nome"] == "Teste"


def test_adicionar_usuario_duplicado(client):
    client.post("/AdicionarUsuario/", params={"email": "dup@gmail.com", "nome": "Dup"})

    resposta = client.post(
        "/AdicionarUsuario/",
        params={"email": "dup@gmail.com", "nome": "Dup"},
    )

    assert resposta.status_code == 400

# Deve listar todos os 0 ou mais usuários
def test_listar_usuarios_todos(client):
    client.post("/ListarUsuarios/")

    resposta = client.post(
        "/ListarUsuarios/"
    )



# o PyTest reconhece client em params e injeta automaticamente a fixture no conftest.py
