from rest_framework.views import APIView
from rest_framework.response import Response
from application_apis.helper.notes_helper import NotesHelper
from application_apis.repositories.notes_repo import NotesRepository
from application_apis.serializers.notes_serializers import NotesViewSerializer
from application_apis.services.notes_services import NotesService

class NoteViews(APIView):
    def __init__(self):
        self.service = NotesService()
        self.helper = NotesHelper()
        self.note_repo = NotesRepository()

    def get(self, request, **kwargs):
        service_data = self.service.get_service(request=request, **kwargs)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return Response(response_data, status=status_code)
    
    def post(self, request, **kwargs):
        service_data = self.service.post_service(request=request)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return Response(response_data, status=status_code)