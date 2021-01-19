from wtforms import Form, SelectField, StringField, IntegerField, validators


class CategoryForm(Form):
    subcategory = SelectField('SubCategory', [validators.required()])
    category = SelectField('Category', [validators.required()])
