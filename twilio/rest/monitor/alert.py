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
from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource


class Alert(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: alert_text
    
        The alert_text
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_generated
    
        The date_generated
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: error_code
    
        The error_code
    
    .. attribute:: log_level
    
        The log_level
    
    .. attribute:: more_info
    
        The more_info
    
    .. attribute:: request_method
    
        The request_method
    
    .. attribute:: request_url
    
        The request_url
    
    .. attribute:: request_variables
    
        The request_variables
    
    .. attribute:: resource_sid
    
        The resource_sid
    
    .. attribute:: response_body
    
        The response_body
    
    .. attribute:: response_headers
    
        The response_headers
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: url
    
        The url
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Alert, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_generated") and self.date_generated:
            self.date_generated = parse_iso_date(self.date_generated)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Alerts(NextGenListResource):
    name = "Alerts"
    mount_name = "alerts"
    key = "alerts"
    instance = Alert

    def __init__(self, *args, **kwargs):
        super(Alerts, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Alert`
        :returns: A placeholder for a :class:`Alert` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete the :class:`Alert`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Alert`
        
        :param date end_date: The end_date
        :param date end_date_after: The end_date>
        :param date end_date_before: The end_date<
        :param date start_date: The start_date
        :param date start_date_after: The start_date>
        :param date start_date_before: The start_date<
        :param str log_level: The log_level
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Alert`
        """
        if "start_date_before" in kwargs:
            kwargs["StartDate<"] = parse_date(kwargs["start_date_before"])
            del kwargs["start_date_before"]
        if "start_date_after" in kwargs:
            kwargs["StartDate>"] = parse_date(kwargs["start_date_after"])
            del kwargs["start_date_after"]
        if "start_date" in kwargs:
            kwargs["StartDate"] = parse_date(kwargs["start_date"])
            del kwargs["start_date"]
        if "end_date_before" in kwargs:
            kwargs["EndDate<"] = parse_date(kwargs["end_date_before"])
            del kwargs["end_date_before"]
        if "end_date_after" in kwargs:
            kwargs["EndDate>"] = parse_date(kwargs["end_date_after"])
            del kwargs["end_date_after"]
        if "end_date" in kwargs:
            kwargs["EndDate"] = parse_date(kwargs["end_date"])
            del kwargs["end_date"]
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Alert` using an iterator
        
        :param date end_date: The end_date
        :param date end_date_after: The end_date>
        :param date end_date_before: The end_date<
        :param date start_date: The start_date
        :param date start_date_after: The start_date>
        :param date start_date_before: The start_date<
        :param str log_level: The log_level
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Alert`
        """
        if "start_date_before" in kwargs:
            kwargs["StartDate<"] = parse_date(kwargs["start_date_before"])
            del kwargs["start_date_before"]
        if "start_date_after" in kwargs:
            kwargs["StartDate>"] = parse_date(kwargs["start_date_after"])
            del kwargs["start_date_after"]
        if "start_date" in kwargs:
            kwargs["StartDate"] = parse_date(kwargs["start_date"])
            del kwargs["start_date"]
        if "end_date_before" in kwargs:
            kwargs["EndDate<"] = parse_date(kwargs["end_date_before"])
            del kwargs["end_date_before"]
        if "end_date_after" in kwargs:
            kwargs["EndDate>"] = parse_date(kwargs["end_date_after"])
            del kwargs["end_date_after"]
        if "end_date" in kwargs:
            kwargs["EndDate"] = parse_date(kwargs["end_date"])
            del kwargs["end_date"]
        return super(Alerts, self).iter(**kwargs)