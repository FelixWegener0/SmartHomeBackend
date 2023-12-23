# SmartHomeBackend

Cron-Job:

Sie können auch einen Cron-Job verwenden, um Ihr Skript beim Booten auszuführen.

Fügen Sie dies zum Crontab hinzu:

bash
Copy code
crontab -e
Fügen Sie die Zeile hinzu:

bash
Copy code
@reboot /pfad/zu/ihrem/skript.sh
Vergewissern Sie sich erneut, dass Sie den absoluten Pfad zu Ihrem Skript verwenden.

Wählen Sie die Methode aus, die am besten zu Ihren Anforderungen passt. Beachten Sie, dass die Methode mit systemd-Service-Units oft als modernere und flexiblere Methode betrachtet wird.
