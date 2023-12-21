class UserDTO:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def create_user_dto_from_request(request):
    username = request.json.get('username')
    password = request.json.get('password')
    return UserDTO(username, password)