# GeoPontos API

Backend para cadastro de pontos geográficos (latitude, longitude e descrição), com CRUD completo de usuários e pontos. Desenvolvido com **FastAPI** e **SQLAlchemy**, com testes automatizados em **PyTest**.


Para executar, instale as dependências do projeto:
```bash
pip install -r requirements.txt, uvicorn app.main:app --reload --port 8080
```


Para executar os testes:
```bash
pytest -v
```

Algumas instruções/detalhes sobre o projeto:
- **PONTOS**: globais, sem dono;
- **ID do Ponto**: gerado automaticamente pelo backend;
- **USER_EMAIL**: único no sistema e funciona como identificador do usuário;
- **AdicionarPonto**: Para executar a função, o usuário deve existir. O parâmetro descricao é opcional;

Na construção do projeto, foram usados os comandos **HTTP(GET/POST/PUT/DELETE)** a fim de praticar.


