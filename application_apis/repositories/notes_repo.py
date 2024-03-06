from application_apis.models.notes import Notes

class NotesRepository:
    def __init__(self):
        self.model = Notes

    def get_all(self):
        return self.query()
    
    def get_all_where(self, filters=[]):
        return self.query(filters)
    
    def get_single(self, filters=[]):
        return self.query(filters).first()
    
    def create(self, data):
        return self.model.objects.create(**data)
    
    def update_where(self, values={}, filters=[]):
        return self.query(filters).update(**values)
    
    def delete_where(self, filters=[]):
        return self.query(filters).delete()
    
    def delete_all(self):
        return self.model.objects.all().delete()
    
    def query(self, filters=[]):
        self.res = self.model.objects.all()
        query = self.res
        for fil in filters:
            query = self.filters(query, fil[0], fil[1])
        return query

    def filters(self, queryset, name, value):
        query = queryset.filter(**{name: value})
        return query