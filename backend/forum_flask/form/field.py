class FormField:
    __fieldtype__ = 'unknown'

class ImageField(FormField):
    __fieldtype__ = 'image'

class EmailField(FormField):
    __fieldtype__ = 'email'

class PasswordField(FormField):
    __fieldtype__ = 'password'