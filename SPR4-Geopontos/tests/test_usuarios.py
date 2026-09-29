def test_adicionar_usuario_sucesso(client):
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

# [TESTE LISTAR USUÁRIOS]
def test_listar_usuarios_inexistentes(client):
    resposta = client.get("/ListarUsuarios/")
    
    assert resposta.status_code == 200
    assert resposta.json() == []

def test_listar_usuarios_todos(client):
    client.post("/AdicionarUsuario/", params={"email": "a@gmail.com", "nome": "Leandro"})
    client.post("/AdicionarUsuario/", params={"email": "b@gmail.com", "nome": "Ferreira"})

    # act test
    resposta = client.get("/ListarUsuarios/")

    # asserts
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert len(corpo) == 2
    emails = [u["email"] for u in corpo]
    assert "a@gmail.com" in emails
    assert "b@gmail.com" in emails

# [TESTE ALTERAR USUÁRIOS]
def test_alterar_usuario_sucesso(client):

    client.post("/AdicionarUsuario/", params={"email": "test@gmail.com", "nome": "Original"})

    resposta = client.put("/AlterarUsuario/", params={"email": "test@gmail.com", "novo_nome": "nomeAlterado"})

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["nome"] == "nomeAlterado"

    # Checa se o nome foi realmente alterado no BD
    lista = client.get("/ListarUsuarios/").json()
    nomes = [u["nome"] for u in lista]
    assert "nomeAlterado" in nomes


def test_alterar_usuario_inexistente(client):
    resposta = client.put("/AlterarUsuario/", params={"email": "emptyTest@gmail.com", "novo_nome": "emptyName"})
    assert resposta.status_code == 404
    
def test_remover_usuario_sucesso(client):
    client.post("/AdicionarUsuario/", params={"email": "test@gmail.com", "nome": "nomeTest"})
    resposta = client.delete("/RemoverUsuario/", params={"email": "test@gmail.com"})
    assert resposta.status_code == 200 # procedimento ocorreu sem falhas

    # Checa se a lista está realmente vazia
    lista = client.get("/ListarUsuarios").json()
    assert not lista

def test_remover_usuario_inexistente(client):
    resposta = client.delete("/RemoverUsuario/", params={"email": "test@gmail.com"})
    assert resposta.status_code == 404


# o PyTest reconhece client em params e injeta automaticamente a fixture no conftest.py
