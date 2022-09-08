import firebase_admin

from firebase_admin import messaging

firebase_admin.initialize_app()

registration_token = input("Please input target device key token: ")
data_notification = messaging.Message(
    token = registration_token,
    notification=messaging.Notification(
        'test-title', 
        'test-body',
    )
)

response = messaging.send(data_notification)

print(response)
print("--> Done")