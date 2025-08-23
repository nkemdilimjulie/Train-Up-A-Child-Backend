# This is where we handle safe donations with SERIALIZABLE isolation.

from django.db import transaction, connection, DatabaseError
import time
from .models import Donation


from django.db import transaction, connection, DatabaseError
import time
from .models import Donation

def safe_donation(child, sponsor, amount, retries=3):
    """
    Process a donation safely using SERIALIZABLE transactions:
    ensures balance updates are safe under concurrent donations.
    """
    for attempt in range(retries):
        try:
            with transaction.atomic():
                with connection.cursor() as cursor:
                    cursor.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;")

                donation = Donation.objects.create(
                    child=child,
                    sponsor=sponsor,
                    amount=amount,
                )

                child.balance += amount
                child.save()

            return donation

        except DatabaseError:
            if attempt < retries - 1:
                time.sleep(0.5)
                continue
            raise
