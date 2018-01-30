import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, sender, acc_details):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = render_to_string(html_content, {'acc_details': acc_details})
        self.sender = sender
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, self.sender, self.recipient_list)
        msg.content_subtype = 'html'
        msg.send()


def send_html_mail(subject, html_content, recipient_list, sender, acc_details):
    EmailThread(subject, html_content, recipient_list, sender, acc_details).start()



