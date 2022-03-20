from notifications.models import PersistentMessage


def send_message(from_, to, message):
    message = PersistentMessage.objects.create(
        author=from_,
        recipient=to,
        message=message)

    message = {
        'author': message.author,
        'recipient': message.recipient,
        'message': message.message
    }
    return message


def get_messages_for_recipient(recipient):
    messages = PersistentMessage.objects.filter(recipient=recipient)
    messages = messages.values('author', 'recipient', 'message')
    return list(messages)
