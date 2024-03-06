from application_apis.helper.notes_helper import NotesHelper
from application_apis.repositories.notes_repo import NotesRepository
from application_apis.serializers.notes_serializers import NotesViewSerializer
from rest_framework import exceptions


class SingleNoteService:

    def __init__(self):
        self.helper = NotesHelper()
        self.note_repo = NotesRepository()

    def get_service(self, request, **kwargs):
        request_data = self.helper.filter_request(request)
        data = {**kwargs, **request_data}
        data = self.helper.get_request_validator(data)
        notes = self.note_repo.get_single([("id", data.get("note_id"))])
        if notes is None:
            raise exceptions.APIException(detail="Note not found", code=404)
        serializer = NotesViewSerializer(notes)
        return {"response_data": serializer.data, "code": 200}

    def put_service(self, request, **kwargs):
        request_data = self.helper.filter_request(request)
        data = {**kwargs, **request_data}
        data = self.helper.update_request_validator(data)
        notes = self.note_repo.get_single([("id", data.get("note_id"))])
        if notes is None:
            raise exceptions.APIException(detail="Note not found", code=404)
        note = self.note_repo.update_where(filters=[("id", data.get("note_id"))], values={"title": data.get("title", notes.title), "body": data.get("body", notes.body)})
        response_data = NotesViewSerializer(note).data
        return {"response_data": response_data, "code": 204}