import logging

from src.GhTrackObject import EmailConf
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class EmailHandler(EmailConf):
    """EmailHandler is use to send email through twilio."""

    """
    This method send email to an configurable email
    :param content: str
    :rtype: :tuple
    """
    def sendEmail(self, content: str) -> tuple:
        try:
            message = Mail(
                from_email=self.fromEmail,
                to_emails=self.to,
                subject=self.subject,
                html_content=content)

            sg = SendGridAPIClient(api_key=self.sendGridApi)
            response = sg.send(message)
            return response.status_code, response.body, response.headers
        except Exception as ex:
            logging.info(f"Api key = {self.sendGridApi}")
            logging.info(f"exception = {ex}")

