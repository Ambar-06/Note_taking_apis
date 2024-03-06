from rest_framework import serializers

from application_apis.models.notes import Notes

class NotesCreateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100, allow_null=True, allow_blank=True)
    body = serializers.CharField(required=True, max_length=500, allow_null=True, allow_blank=True)

    def validator(self, data):
        serializer = NotesCreateSerializer(data=data)
        if serializer.is_valid():
            return data
        else:
            raise serializers.ValidationError(serializer.errors)

class NotesUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, max_length=100, allow_null=True, allow_blank=True)
    body = serializers.CharField(required=False, max_length=500, allow_null=True, allow_blank=True)

    def validator(self, data):
        serializer = NotesUpdateSerializer(data=data)
        if serializer.is_valid():
            return data
        else:
            raise serializers.ValidationError(serializer.errors)
        
class NotesFilterSerializer(serializers.Serializer):
    note_id = serializers.IntegerField(required=False, allow_null=True)
    title = serializers.CharField(required=False, max_length=100, allow_null=True, allow_blank=True)

    def validator(self, data):
        serializer = NotesFilterSerializer(data=data)
        if serializer.is_valid():
            return data
        else:
            raise serializers.ValidationError(serializer.errors)
        
class NotesViewSerializer(serializers.ModelSerializer):
    note_id = serializers.IntegerField(source="id", read_only=True)
    note_title = serializers.CharField(source="title", read_only=True)
    note_content = serializers.CharField(source="body", read_only=True)


    class Meta:
        model = Notes
        fields = ('note_id', 'note_title', 'note_content', 'updated_at', 'created_at')
