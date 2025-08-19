# This is where we handle safe donations with SERIALIZABLE isolation.

from django.db import transaction, connection, DatabaseError
import time
from .models import Donation


def safe_donation(child, sponsor, amount, retries=3):
    """
    Process a donation safely using SERIALIZABLE transactions: when two
    sponsors try to donate to the same child, one will wait and retry.
    This prevents omissions ? or double donations?.
    Retries if PostgreSQL detects conflicts.
    """
    for attempt in range(retries):
        try:
            with transaction.atomic():
                # Force SERIALIZABLE isolation for this transaction
                with connection.cursor() as cursor:
                    cursor.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;")

                donation = Donation.objects.create(
                    child=child,
                    sponsor=sponsor,
                    amount=amount,
                )

                # Safely update child’s balance
                child.balance += amount
                child.save()

            return donation

        except DatabaseError:
            if attempt < retries - 1:
                time.sleep(0.5)  # wait before retry
                continue
            raise
