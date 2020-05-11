from django.contrib import admin

# Register your models here.
from .models import product
from .models import customer
from .models import case
from .models import salesperson
from .models import Employee
from .models import resolution
from .models import caseComment
from .models import purchase
from .models import relate
from .models import support
from .models import assign
from .models import comment
from .models import sell
from .models import apply
from .models import check

admin.site.register(product)
admin.site.register(customer)
admin.site.register(case)
admin.site.register(salesperson)
admin.site.register(Employee)
admin.site.register(resolution)
admin.site.register(caseComment)
admin.site.register(purchase)
admin.site.register(relate)
admin.site.register(support)
admin.site.register(assign)
admin.site.register(comment)
admin.site.register(sell)
admin.site.register(apply)
admin.site.register(check)