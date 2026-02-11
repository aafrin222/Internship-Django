from django.db import models

# 1. User Table: Manages Admin and User roles using standard models.Model
class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    
    # Basic credentials and profile info
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128) 
    email = models.EmailField(unique=True)
    
    # Specific fields from your project requirements
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    contact_info = models.CharField(max_length=255, blank=True, null=True) 
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


# 2. Parking Lot Table: Defines infrastructure and capacity.
class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    location_coordinates = models.CharField(max_length=255) 
    total_capacity = models.PositiveIntegerField()
    layout_description = models.TextField(blank=True) 

    def __str__(self):
        return self.name
    

# 3. Parking Slot Table: Manages specific space types and status.
class ParkingSlot(models.Model):
    SLOT_TYPES = (
        ('regular', 'Regular'),
        ('ev', 'Electric Vehicle'),
        ('handicap', 'Handicap-accessible'),
    )
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
    )
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE, related_name='slots')
    slot_id_code = models.CharField(max_length=50, unique=True) 
    slot_type = models.CharField(max_length=20, choices=SLOT_TYPES, default='regular')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.slot_id_code} in {self.parking_lot.name}"
    

# 4. Reservation Table: Tracks booking durations and verification.
class Reservation(models.Model):
    DURATION_CHOICES = (
        ('hourly', 'Hourly'),
        ('daily', 'Daily'),
        ('monthly', 'Monthly'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    duration_type = models.CharField(max_length=10, choices=DURATION_CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    verification_qr_code = models.CharField(max_length=255, unique=True) 
    is_active = models.BooleanField(default=True)


# 5. Payment Table: Records cashless transactions and history.
class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50) 
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True) 


# 6. Notification Table: Sends alerts to users and admins.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


# 7. Analytics Log: Captures data for the admin dashboard.
class OccupancyLog(models.Model):
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    occupancy_count = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True) 