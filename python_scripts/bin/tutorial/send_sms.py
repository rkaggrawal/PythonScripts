#!/usr/bin/python

from twilio.rest import TwilioRestClient

client = TwilioRestClient()

client.message.create(from_="08806940079",
                      to="08329822923",
                      body="First sms"

                      )