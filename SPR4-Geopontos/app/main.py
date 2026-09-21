# POST/AdicionarUsuario/?email/nome => fastAPI chama getdb com nome/user para iniciar sessão => função consulta usuarios procurando esse email =>
# Se achar → erro 400. Se não achar → cria Usuario(...), salva com db.add + db.commit, devolve o JSON
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Usuario

app = FastAPI(title="GeoPontos API")

# Cria as tabelas no geopontos.db quando o banco subir, olhando as classes existentes
Base.metadata.create_all(bind=engine)

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