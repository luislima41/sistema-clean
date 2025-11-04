from domain.entities.user import User

class CreateUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, username, email):
        user = User(username, email)
        self.repository.save(user)
        return f"Usuário {username} criado com sucesso!"