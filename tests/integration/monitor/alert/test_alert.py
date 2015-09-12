# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

import unittest
from datetime import datetime
from twilio.ext.holodeck import Holodeck
from twilio.rest.monitor.client import MonitorClient
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class AlertIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "alert_text": "sourceComponent=14100&httpResponse=500&url=https%3A%2F%2F2Fv1%2Fsms%2Ftwilio&ErrorCode=11200&LogLevel=ERROR&Msg=Internal+Server+Error&EmailNotification=false",
            "api_version": "2008-08-01",
            "date_created": "2015-08-29T17:20:16Z",
            "date_generated": "2015-08-29T17:20:14Z",
            "date_updated": "2015-08-29T17:20:16Z",
            "error_code": "11200",
            "log_level": "error",
            "more_info": "https://www.twilio.com/docs/errors/11200",
            "request_method": "POST",
            "request_url": "https://www.example.com",
            "request_variables": "ToCountry=US&ToState=CA&SmsMessageSid=SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&NumMedia=0&ToCity=&FromZp&FromState=CA&SmsStatus=received&FromCity=SAN+FRANCISCO&Body=plan+5+potato&FromCountry=US&To=%2B1&ToZip=&NumSegments=1&MessageSid=SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&AccountSid=ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&From=%2B1&ApiVersion=2010-04-01",
            "resource_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "response_body": "blahblah",
            "response_headers": "X-Cache=MISS+from+ip-10-.Google+Frontend&X-Cache-Lookup=MISS+from+ip&Alt-Svc=quic%3D%22%3A443%22%3B+p%3D%221%22%3B+ma%3D604800&Content-Length=323&Content-Type=text%2Fhtml%3B+charset%3DUTF-8&Date=Sat%2C+29+Aug+2015+17%3A20%3A16+GMT&Alternate-Protocol=443%3Aquic%2Cp%3D1",
            "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://monitor.twilio.com/v1/Alerts/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .alerts.get("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://monitor.twilio.com/v1/Alerts/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "alert_text": "sourceComponent=14100&httpResponse=500&url=https%3A%2F%2F2Fv1%2Fsms%2Ftwilio&ErrorCode=11200&LogLevel=ERROR&Msg=Internal+Server+Error&EmailNotification=false",
            "api_version": "2008-08-01",
            "date_created": "2015-08-29T17:20:16Z",
            "date_generated": "2015-08-29T17:20:14Z",
            "date_updated": "2015-08-29T17:20:16Z",
            "error_code": "11200",
            "log_level": "error",
            "more_info": "https://www.twilio.com/docs/errors/11200",
            "request_method": "POST",
            "request_url": "https://www.example.com",
            "request_variables": "ToCountry=US&ToState=CA&SmsMessageSid=SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&NumMedia=0&ToCity=&FromZp&FromState=CA&SmsStatus=received&FromCity=SAN+FRANCISCO&Body=plan+5+potato&FromCountry=US&To=%2B1&ToZip=&NumSegments=1&MessageSid=SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&AccountSid=ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&From=%2B1&ApiVersion=2010-04-01",
            "resource_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "response_body": "blahblah",
            "response_headers": "X-Cache=MISS+from+ip-10-.Google+Frontend&X-Cache-Lookup=MISS+from+ip&Alt-Svc=quic%3D%22%3A443%22%3B+p%3D%221%22%3B+ma%3D604800&Content-Length=323&Content-Type=text%2Fhtml%3B+charset%3DUTF-8&Date=Sat%2C+29+Aug+2015+17%3A20%3A16+GMT&Alternate-Protocol=443%3Aquic%2Cp%3D1",
            "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "url": "https://monitor.twilio.com/v1/Alerts/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .alerts.get("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.alert_text)
        self.assertEqual(u"sourceComponent=14100&httpResponse=500&url=https%3A%2F%2F2Fv1%2Fsms%2Ftwilio&ErrorCode=11200&LogLevel=ERROR&Msg=Internal+Server+Error&EmailNotification=false", instance.alert_text)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("2015-08-29T17:20:16Z"), instance.date_created)
        self.assertIsNotNone(instance.date_generated)
        self.assertEqual(parse_iso_date("2015-08-29T17:20:14Z"), instance.date_generated)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("2015-08-29T17:20:16Z"), instance.date_updated)
        self.assertIsNotNone(instance.error_code)
        self.assertEqual(u"11200", instance.error_code)
        self.assertIsNotNone(instance.log_level)
        self.assertEqual(u"error", instance.log_level)
        self.assertIsNotNone(instance.more_info)
        self.assertEqual(u"https://www.twilio.com/docs/errors/11200", instance.more_info)
        self.assertIsNotNone(instance.request_method)
        self.assertEqual(u"POST", instance.request_method)
        self.assertIsNotNone(instance.request_url)
        self.assertEqual(u"https://www.example.com", instance.request_url)
        self.assertIsNotNone(instance.request_variables)
        self.assertEqual(u"ToCountry=US&ToState=CA&SmsMessageSid=SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&NumMedia=0&ToCity=&FromZp&FromState=CA&SmsStatus=received&FromCity=SAN+FRANCISCO&Body=plan+5+potato&FromCountry=US&To=%2B1&ToZip=&NumSegments=1&MessageSid=SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&AccountSid=ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&From=%2B1&ApiVersion=2010-04-01", instance.request_variables)
        self.assertIsNotNone(instance.resource_sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.resource_sid)
        self.assertIsNotNone(instance.response_body)
        self.assertEqual(u"blahblah", instance.response_body)
        self.assertIsNotNone(instance.response_headers)
        self.assertEqual(u"X-Cache=MISS+from+ip-10-.Google+Frontend&X-Cache-Lookup=MISS+from+ip&Alt-Svc=quic%3D%22%3A443%22%3B+p%3D%221%22%3B+ma%3D604800&Content-Length=323&Content-Type=text%2Fhtml%3B+charset%3DUTF-8&Date=Sat%2C+29+Aug+2015+17%3A20%3A16+GMT&Alternate-Protocol=443%3Aquic%2Cp%3D1", instance.response_headers)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_delete_request_validation(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .alerts.delete("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "DELETE",
            "https://monitor.twilio.com/v1/Alerts/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_delete_can_parse_response(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(204, "{}"))
        
        query = client \
            .alerts.delete("NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertTrue(query.execute())

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "alerts": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "alert_text": "sourceComponent=14100&httpResponse=500&url=https%3A%2F%2Fcommunicate-indonesia-staging.appspot.com%2Fv1%2Fsms%2Ftwilio&ErrorCode=11200&LogLevel=ERROR&Msg=Internal+Server+Error&EmailNotification=false",
                    "api_version": "2008-08-01",
                    "date_created": "2015-08-29T17:20:16Z",
                    "date_generated": "2015-08-29T17:20:14Z",
                    "date_updated": "2015-08-29T17:20:16Z",
                    "error_code": "11200",
                    "log_level": "error",
                    "more_info": "https://www.twilio.com/docs/errors/11200",
                    "request_method": "POST",
                    "request_url": "https://www.example.com",
                    "resource_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://monitor.twilio.com/v1/Alerts/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0",
                "key": "alerts",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .alerts.list(
                log_level="log_level",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].alert_text)
        self.assertEqual(u"sourceComponent=14100&httpResponse=500&url=https%3A%2F%2Fcommunicate-indonesia-staging.appspot.com%2Fv1%2Fsms%2Ftwilio&ErrorCode=11200&LogLevel=ERROR&Msg=Internal+Server+Error&EmailNotification=false", instances[0].alert_text)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2008-08-01", instances[0].api_version)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("2015-08-29T17:20:16Z"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_generated)
        self.assertEqual(parse_iso_date("2015-08-29T17:20:14Z"), instances[0].date_generated)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("2015-08-29T17:20:16Z"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].error_code)
        self.assertEqual(u"11200", instances[0].error_code)
        self.assertIsNotNone(instances[0].log_level)
        self.assertEqual(u"error", instances[0].log_level)
        self.assertIsNotNone(instances[0].more_info)
        self.assertEqual(u"https://www.twilio.com/docs/errors/11200", instances[0].more_info)
        self.assertIsNotNone(instances[0].request_method)
        self.assertEqual(u"POST", instances[0].request_method)
        self.assertIsNotNone(instances[0].request_url)
        self.assertEqual(u"https://www.example.com", instances[0].request_url)
        self.assertIsNotNone(instances[0].resource_sid)
        self.assertEqual(u"SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].resource_sid)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "alerts": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "alert_text": "sourceComponent=14100&httpResponse=500&url=https%3A%2F%2Fcommunicate-indonesia-staging.appspot.com%2Fv1%2Fsms%2Ftwilio&ErrorCode=11200&LogLevel=ERROR&Msg=Internal+Server+Error&EmailNotification=false",
                    "api_version": "2008-08-01",
                    "date_created": "2015-08-29T17:20:16Z",
                    "date_generated": "2015-08-29T17:20:14Z",
                    "date_updated": "2015-08-29T17:20:16Z",
                    "error_code": "11200",
                    "log_level": "error",
                    "more_info": "https://www.twilio.com/docs/errors/11200",
                    "request_method": "POST",
                    "request_url": "https://www.example.com",
                    "resource_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "url": "https://monitor.twilio.com/v1/Alerts/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            ],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0",
                "key": "alerts",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .alerts.list(
                log_level="log_level",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://monitor.twilio.com/v1/Alerts",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "EndDate<": "2008-01-01",
                "EndDate>": "2008-01-03",
                "LogLevel": "log_level",
                "StartDate": "2008-01-02",
                "StartDate<": "2008-01-01",
                "StartDate>": "2008-01-03"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "alerts": [],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0",
                "key": "alerts",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .alerts.list(
                log_level="log_level",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = MonitorClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "alerts": [],
            "meta": {
                "first_page_url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0",
                "key": "alerts",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://monitor.twilio.com/v1/Alerts?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .alerts.list(
                log_level="log_level",
                start_date=datetime(2008, 1, 2, 0, 0),
                start_date_before=datetime(2008, 1, 1, 0, 0),
                start_date_after=datetime(2008, 1, 3, 0, 0),
                end_date=datetime(2008, 1, 2, 0, 0),
                end_date_before=datetime(2008, 1, 1, 0, 0),
                end_date_after=datetime(2008, 1, 3, 0, 0)
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://monitor.twilio.com/v1/Alerts",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "EndDate": "2008-01-02",
                "EndDate<": "2008-01-01",
                "EndDate>": "2008-01-03",
                "LogLevel": "log_level",
                "StartDate": "2008-01-02",
                "StartDate<": "2008-01-01",
                "StartDate>": "2008-01-03"
            },
        )