from wtforms import *

# Borrowed from http://wtforms.simplecodes.com/docs/0.6/fields.html#custom-fields
class TagListField(Field):
    widget = widgets.TextInput()

    def _value(self):
        if self.data:
            return self.data.join(u',')
        else:
            return u''

    def process_formdata(self, valuelist):
        self.data = self._parse_comma_sep_list(valuelist)
        self.data = list(self._remove_duplicates(self.data))

    @classmethod
    def _parse_comma_sep_list(cls, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]

    @classmethod
    def _remove_duplicates(cls, seq):
        """Remove duplicates in a case insensitive, but case preserving manner"""
        d = {}
        for item in seq:
            if item.lower() not in d:
                d[item.lower()] = True
                yield item

class ResourceForm(Form):
    resourceType = SelectField('Resource Type', 
        choices=[('File', 'file'), ('Web Resource', 'resource')])
    url = TextField('Url', [validators.URL(require_tld=False)])
    file = FileField('Resource File')

class CreateForm(Form):
    title = TextField('Resource Name', [validators.required()])
    description = TextAreaField('Description')
    tags = TagListField('Tags')
    resources = FieldList(FormField(ResourceForm))

    def validate_resources(form, field):
        return (field.url.data != None) != (field.file.data != None)