from django.contrib import admin


from .models import Person, Child, Teacher, Class

admin.site.register(Person)
admin.site.register(Child)
admin.site.register(Teacher)
admin.site.register(Class)


