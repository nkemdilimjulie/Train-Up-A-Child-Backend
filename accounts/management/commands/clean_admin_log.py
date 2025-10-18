from django.core.management.base import BaseCommand
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class Command(BaseCommand):
    help = "Clean up admin log entries with missing users"

    def handle(self, *args, **options):
        # Count how many entries exist before cleanup
        total_before = LogEntry.objects.count()

        # Find all orphaned logs (user_id not in auth_user)
        valid_user_ids = User.objects.values_list("id", flat=True)
        orphaned_logs = LogEntry.objects.exclude(user_id__in=valid_user_ids)

        count = orphaned_logs.count()
        orphaned_logs.delete()

        total_after = LogEntry.objects.count()

        self.stdout.write(self.style.SUCCESS(
            f"🧹 Cleaned {count} orphaned admin log entries."
        ))
        self.stdout.write(f"Total before: {total_before}, after: {total_after}")
