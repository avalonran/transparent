class ModelMixin:
    def to_dict(self):
        '''数据转字典'''
        data = []
        for field in self._meta.fields:
            name = field.attname
            # value = self.__dict__[name]
            value = getattr(self, name)
            data[name] = value
        return data
