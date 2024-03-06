from application_apis.helper.notes_helper import NotesHelper
from application_apis.repositories.notes_repo import NotesRepository
from application_apis.serializers.notes_serializers import NotesViewSerializer


class NotesService:

    def __init__(self):
        self.helper = NotesHelper()
        self.note_repo = NotesRepository()

    def get_service(self, request, **kwargs):
        request_data = self.helper.filter_request(request)
        data = {**kwargs, **request_data}
        data = self.helper.get_request_validator(data)
        if data.get("title") and data.get("title") != "" and data.get("title") is not None:
            notes = self.note_repo.get_all_where([("title__icontains", data.get("title"))])
        else:
            notes = self.note_repo.get_all()
        serializer = NotesViewSerializer(notes, many=True)
        return {"response_data": serializer.data, "code": 200}

    def post_service(self, request, **kwargs):
        request_data = self.helper.filter_request(request)
        data = {**kwargs, **request_data}
        data = self.helper.post_request_validate(data)
        note = self.note_repo.create(data)
        response_data = NotesViewSerializer(note).data
        return {"response_data": response_data, "code": 201}