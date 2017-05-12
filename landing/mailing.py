import sendgrid
from sendgrid.helpers.mail.mail import Mail, Email, Personalization, Substitution, Content

API_KEY = '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'

def send_welcome(email, nome):

    def prepare_data(email, nome):

        mail = Mail()

        mail.set_from(Email('contato@trokey.com.br'))

        mail.set_subject('Seu registro no trokey.com.br')

        mail.set_template_id('582e8167-1737-4482-afd8-3145cacbd3dd')

        personalization = Personalization()

        mails_bcc = ['picobasa@gmail.com', 'oswaldo.neto@gmail.com',]
        for mail_bcc in mails_bcc:
            personalization.add_bcc(Email(mail_bcc))

        personalization.add_to(Email(email))

        personalization.add_substitution(Substitution('nome', nome ))

        mail.add_personalization(personalization)

        mail.add_content(Content("text/html", " "))

        return mail.get()

    sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

    # prepare api send request data
    data = prepare_data(email, nome)

    # api send call
    response = sg.client.mail.send.post(request_body=data)
