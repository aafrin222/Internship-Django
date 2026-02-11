from django.contrib import admin
from.models import User,ParkingLot,ParkingSlot,Reservation,Payment,Notification,OccupancyLog

# Register your models here.
admin.site.register(User)
admin.site.register(ParkingLot)
admin.site.register(ParkingSlot)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Notification)
admin.site.register(OccupancyLog)
