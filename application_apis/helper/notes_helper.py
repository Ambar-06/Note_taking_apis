from application_apis.serializers.notes_serializers import NotesCreateSerializer, NotesFilterSerializer, NotesUpdateSerializer

class NotesHelper:
    def __init__(self):
        self.serializer = NotesCreateSerializer()
        self.filter_serializer = NotesFilterSerializer()
        self.update_serializer = NotesUpdateSerializer()

    def post_request_validate(self, data):
        return self.serializer.validator(data)
    
    def get_request_validator(self, data):
        return self.filter_serializer.validator(data)
    
    def update_request_validator(self, data):
        return self.update_serializer.validator(data)

    
    def filter_request(self, request):
        if request.method == 'GET':
            request_data = {key : value for key, value in request.query_params.items()}
            return request_data
        else:
            return request.data