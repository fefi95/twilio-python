# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.v2010.account.message.media import (
    Media,
    MediaList,
)
from twilio.rest.resources.base import ListResource


class Message(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that sent this message.
    
    .. attribute:: api_version
    
        The version of the Twilio API used to process the message.
    
    .. attribute:: body
    
        The text body of the message. Up to 1600 characters long.
    
    .. attribute:: date_created
    
        The date that this resource was created, given in RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given in RFC 2822 format.
    
    .. attribute:: date_sent
    
        The date that the message was sent. For incoming messages, this is the
        date that Twilio received the message. The date is given in RFC 2822
        format.
    
    .. attribute:: direction
    
        The direction of this message. `inbound` for incoming messages,
        `outbound-api` for messages initiated via the REST API, `outbound-call`
        for messages initiated during a call or `outbound-reply` for messages
        initiated in response to an incoming message.
    
    .. attribute:: error_code
    
        The error code, if any, associated with your message. If your message
        status is `failed` or `undelivered`, the ErrorCode can give you more
        information about the failure. The value will be null if the message was
        delivered successfully.
    
    .. attribute:: error_message
    
        The human readable description of the ErrorCode. If the message status
        is `failed` or `undelivered` it will have one of the values described
        below, otherwise it will be null.
    
    .. attribute:: from
    
        The phone number (in E.164 format) or alphanumeric sender ID that
        initiated the message. For incoming messages, this will be the remote
        phone. For outgoing messages, this will be one of your Twilio phone
        numbers or the alphanumeric sender ID used.
    
    .. attribute:: num_media
    
        This property indicates the number of media files associated with the
        message. Each message may send up to 10 media files.
    
    .. attribute:: num_segments
    
        This property indicates the number of messages used to deliver the body
        specified.  If your body is too large to be sent as a single SMS
        message, it will be segmented and charged accordingly.
    
    .. attribute:: price
    
        The amount billed for the message, in the currency associated with the
        account.  Note that your account will be charged for each segment sent
        to the handset.
    
    .. attribute:: price_unit
    
        The currency in which `Price` is measured, in ISO 4127 format (e.g.
        `usd`, `eur`, `jpy`).
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: status
    
        The status of this message. Either `queued`, `sending`, `sent`,`failed`,
        `delivered`,     `undelivered`, `receiving` or `received`.
    
    .. attribute:: subresource_uris
    
        The subresource_uris
    
    .. attribute:: to
    
        The phone number that received the message in E.164 format. For incoming
        messages, this will be one of your Twilio phone numbers. For outgoing
        messages, this will be the remote phone.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"
    DELIVERED = "delivered"
    FAILED = "failed"
    INBOUND = "inbound"
    OUTBOUND_API = "outbound-api"
    OUTBOUND_CALL = "outbound-call"
    OUTBOUND_REPLY = "outbound-reply"
    QUEUED = "queued"
    RECEIVED = "received"
    RECEIVING = "receiving"
    SENDING = "sending"
    SENT = "sent"
    UNDELIVERED = "undelivered"
    subresources = [
        MediaList
    ]

    def load(self, *args, **kwargs):
        super(Message, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)
        
        if hasattr(self, "date_sent") and self.date_sent:
            self.date_sent = parse_iso_date(self.date_sent)

    def delete(self):
        """
        Deletes a message record from your account
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()

    def update(self, **kwargs):
        """
        To redact a message-body from a post-flight message record, post to the message instance resource with an empty body
        
        :param str body: The body
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Message`
        """
        return self.update_instance(kwargs)

    def redact(self, **kwargs):
        """ An alias to update """
        return self.update(body='', **kwargs)


class Messages(ListResource):
    name = "Messages"
    mount_name = "messages"
    key = "messages"
    instance = Message

    def __init__(self, *args, **kwargs):
        super(Messages, self).__init__(*args, **kwargs)

    def create(self, to, from_, **kwargs):
        """
        Send a message from the account used to make the request
        
        :param str application_sid: Twilio the POST MessageSid as well as MessageStatus
            to the URL in the MessageStatusCallback property of this Application
        :param str body: The body
        :param str from_: A Twilio phone number or alphanumeric sender ID enabled for
            the type of message you wish to send.
        :param str media_url: The media_url
        :param str status_callback: The URL that Twilio will POST to each time your
            message status changes
        :param str to: The destination phone number. Format with a '+' and country code
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Message`
        """
        kwargs["To"] = to
        kwargs["From"] = from_
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Deletes a message record from your account
        
        :param str sid: The message sid that uniquely identifies the message to delete
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def get(self, sid):
        """
        Fetch a message belonging to the account used to make the request
        
        :param str sid: The message Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Message`
        :returns: A placeholder for a :class:`Message` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of messages belonging to the account used to make the request
        
        :param date date_sent: Filter messages sent by this date
        :param date date_sent_after: The date_sent>
        :param date date_sent_before: The date_sent<
        :param str from_: Only show messages from this phone number
        :param str to: Filter by messages to this number
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Message`
        """
        if "from_" in kwargs:
            kwargs["From"] = kwargs["from_"]
            del kwargs["from_"]
        if "date_sent_before" in kwargs:
            kwargs["DateSent<"] = parse_date(kwargs["date_sent_before"])
            del kwargs["date_sent_before"]
        if "date_sent_after" in kwargs:
            kwargs["DateSent>"] = parse_date(kwargs["date_sent_after"])
            del kwargs["date_sent_after"]
        if "date_sent" in kwargs:
            kwargs["DateSent"] = parse_date(kwargs["date_sent"])
            del kwargs["date_sent"]
        return self.get_instances(kwargs)

    def update(self, sid, **kwargs):
        """
        To redact a message-body from a post-flight message record, post to the message instance resource with an empty body
        
        :param str body: The body
        :param str sid: The message to redact
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Message`
        """
        return self.update_instance(sid, kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of messages belonging to the account used to make the request
        
        :param date date_sent: Filter messages sent by this date
        :param date date_sent_after: The date_sent>
        :param date date_sent_before: The date_sent<
        :param str from_: Only show messages from this phone number
        :param str to: Filter by messages to this number
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Message`
        """
        if "from_" in kwargs:
            kwargs["From"] = kwargs["from_"]
            del kwargs["from_"]
        if "date_sent_before" in kwargs:
            kwargs["DateSent<"] = parse_date(kwargs["date_sent_before"])
            del kwargs["date_sent_before"]
        if "date_sent_after" in kwargs:
            kwargs["DateSent>"] = parse_date(kwargs["date_sent_after"])
            del kwargs["date_sent_after"]
        if "date_sent" in kwargs:
            kwargs["DateSent"] = parse_date(kwargs["date_sent"])
            del kwargs["date_sent"]
        return super(Messages, self).iter(**kwargs)

    def redact(self, sid, **kwargs):
        """ An alias to update """
        return self.update(sid, body='', **kwargs)