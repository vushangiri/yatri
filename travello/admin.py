from django.contrib import admin
from travello.models import contact,passhash,subscribe,bookings,Destination,comments,budgetplaces,nationalparks,religious,trecking,honeymoon,familyplaces, user_details

# Register your models here.
admin.site.register(contact)
admin.site.register(passhash)
admin.site.register(subscribe)
admin.site.register(bookings)
admin.site.register(Destination)
admin.site.register(comments)
admin.site.register(honeymoon)
admin.site.register(budgetplaces)
admin.site.register(religious)
admin.site.register(trecking)
admin.site.register(familyplaces)
admin.site.register(nationalparks)
admin.site.register(user_details)

