# POST/AdicionarUsuario/?email/nome => fastAPI chama getdb com nome/user para iniciar sessão => função consulta usuarios procurando esse email =>
# Se achar → erro 400. Se não achar → cria Usuario(...), salva com db.add + db.commit, devolve o JSON
from app.models import Usuario
from sqlalchemy.orm import Session
from app.models import Usuario, Ponto 
from app.database import Base, engine, get_db
from fastapi import Depends, FastAPI, HTTPException


app = FastAPI(title="GeoPontos API")

# Cria as tabelas no geopontos.db quando o banco subir, olhando as classes existentes
Base.metadata.create_all(bind=engine)

# [SEÇÃO DE PONTOS] ===============
@app.post("/AdicionarPonto/")
def adicionar_ponto(
    latitude: float,
    longitude: float,
    email: str,
    descricao: str = "no description",
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code = 404, detail= "user not found")

    novo_ponto = Ponto(latitude=latitude, longitude=longitude, descricao=descricao)
    db.add(novo_ponto)
    db.commit()
    db.refresh(novo_ponto)

    return {
        "id": novo_ponto.id,
        "latitude": novo_ponto.latitude,
        "longitude": novo_ponto.longitude,
        "descricao": novo_ponto.descricao,
    }

@app.get("/ListarPontos/")
def listar_pontos(db: Session = Depends(get_db)):
    pontos = db.query(Ponto).all()
    return [
        {"id": p.id, 
        "latitude": p.latitude, 
        "longitude": p.longitude, 
        "descricao": p.descricao}
        for p in pontos
    ]

@app.put("/AlterarPonto/")
def alterar_ponto(
    id: str, 
    latitude: float = None, 
    longitude: float = None, 
    descricao: str=None, 
    db: Session = Depends(get_db)
):
    ponto = db.query(Ponto).filter(Ponto.id == id).first()
    if not ponto:
        raise HTTPException(status_code = 404, detail="point wasnt found")
    
    if latitude:
        ponto.latitude = latitude
    if longitude:
        ponto.longitude = longitude
    if descricao:
        ponto.descricao = descricao

    db.commit()
    db.refresh(ponto)
    
    return {"id": ponto.id, "latitude": ponto.latitude, "longitude": ponto.longitude, "descricao": ponto.descricao}

@app.delete("/RemoverPonto/")
def remover_ponto(id: str, user: str, db:Session = Depends(get_db)):
    ponto = db.query(Ponto).filter(Ponto.id == id).first()
    if not ponto:
        raise HTTPException(status_code = 404, detail= "point wasnt found")
    
    db.delete(ponto)
    db.commit()

    return {"detail": "ponto removido!" }

# [SEÇÃO DE USUÁRIOS] ===============
@app.post("/AdicionarUsuario/") # get_db é chamado pelo fast API automaticamente, pega a sessão de yield_db e passa como parâmetro db na função
def adicionar_usuario(email: str, nome: str, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado com esse email")

    novo_usuario = Usuario(email=email, nome=nome)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return {"id": novo_usuario.id, "email": novo_usuario.email, "nome": novo_usuario.nome}

@app.get("/ListarUsuarios/") # GET para listing
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [{"id": u.id, "email": u.email, "nome": u.nome} for u in usuarios]

@app.put("/AlterarUsuario/")
def alterar_usuario(email:str, novo_nome: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="User not found");

    usuario.nome = novo_nome
    db.commit()
    db.refresh(usuario)

    return {"id": usuario.id, "email": usuario.email, "nome": usuario.nome}

@app.delete("/RemoverUsuario/")
def remover_usuario(email: str, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(usuario)
    db.commit()

    return {"detail": "Usuário removido com sucesso!"}

