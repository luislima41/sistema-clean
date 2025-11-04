from application.use_cases.create_user import CreateUser
from application.use_cases.list_users import ListUsers
from infrastructure.repositories.user_repository import UserRepository

repo = UserRepository()
create_user_uc = CreateUser(repo)
list_users_uc = ListUsers(repo)

def criar_usuario(username, email):
    print(create_user_uc.execute(username, email))

def listar_usuarios():
    users = list_users_uc.execute()
    print("Usuários cadastrados:")
    for u in users:
        print(f"- {u.username} ({u.email})")