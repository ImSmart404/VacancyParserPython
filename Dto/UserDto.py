class UserDTO:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def create_user_dto_from_request(request):
    username = request.form.get('username')
    password = request.form.get('password')
    return UserDTO(username, password)