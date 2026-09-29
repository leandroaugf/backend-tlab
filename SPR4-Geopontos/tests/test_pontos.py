def test_adicionar_ponto_sucesso(client):
    # Criação do usuário
    client.post(
        "/AdicionarUsuario/",
        params={"email": "test@gmail.com", "nome": "admin"},
    )

    # Criação do ponto
    resposta = client.post(
        "/AdicionarPonto/", 
        params={ "latitude": 1., "longitude": 1., "email": "test@gmail.com", "descricao": "testPoint" })

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["latitude"] == 1

def test_adicionar_ponto_usuario_inexistente(client):
    resposta = client.post(
        "/AdicionarPonto/", 
        params={"latitude": 1., "longitude": 1., "email": "test@gmail.com", "descricao": "testPoint" })
    assert resposta.status_code == 404 # USER NOT FOUND

def test_listar_pontos_sucesso(client):
    client.post("/AdicionarUsuario/", params={"email": "test@gmail.com", "nome": "admin"})
    client.post("/AdicionarUsuario/", params={"email": "test2@gmail.com", "nome": "admin2"})
    client.post("/AdicionarPonto/", params={"id":"1", "latitude": 1, "longitude": 1, "email": "test@gmail.com", "descricao": "testPoint" } )
    client.post("/AdicionarPonto/", params={"id":"2", "latitude": 2, "longitude": 2, "email": "test2@gmail.com", "descricao": "testPoint2" } )

    resposta = client.get("/ListarPontos/")
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert len(corpo) == 2
    descricoes = [u["descricao"] for u in corpo]
    assert "testPoint" in descricoes
    assert "testPoint2" in descricoes

def test_listar_pontos_inexistentes(client):
    resposta = client.get("/ListarPontos/")
    assert resposta.status_code == 200
    assert resposta.json() == []


def test_alterar_ponto_sucesso(client):
    client.post("/AdicionarUsuario/", params={"email": "test@gmail.com", "nome": "admin"})
    criacao = client.post( "/AdicionarPonto/", params={"latitude": 1, "longitude": 1, "email": "test@gmail.com","descricao": "testPoint" } )
    id_ponto = criacao.json()["id"]

    resposta = client.put("/AlterarPonto/", params={"id": id_ponto, "latitude": 1.5, "longitude": 1.5})
    assert resposta.status_code == 200
    
    # Checa se um dos valores foi realmente alterado
    assert resposta.json()["latitude"] == 1.5

def test_alterar_ponto_inexistente(client):
    resposta = client.put("/AlterarPonto/", params={"id": "NONE", "latitude": 1.5, "longitude": 1.5})
    assert resposta.status_code == 404

def test_remover_ponto_sucesso(client):
    client.post("/AdicionarUsuario/", params={"email": "test@gmail.com", "nome": "admin"})
    criacao = client.post( "/AdicionarPonto/", params={"id":"1", "latitude": 1, "longitude": 1, "email": "test@gmail.com","descricao": "testPoint" } )

    id_ponto = criacao.json()["id"]
    client.delete("/RemoverPonto/", params={"id":id_ponto, "user": "test@gmail.com"}) 

    # Confere se o ponto foi realmente removido
    pontos = client.get("/ListarPontos/").json()
    assert pontos == []

def test_remover_ponto_inexistente(client):
    resposta = client.delete("/RemoverPonto/", params={"id": "NONE", "user": "test@gmail.com"})
    assert resposta.status_code == 404