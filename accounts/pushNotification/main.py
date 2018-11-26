from txfcm import TXFCMNotification
from twisted.internet import reactor
from .baseapi import BaseAPI

push_service = TXFCMNotification(api_key="AAAA3Mgl_0Y:APA91bFKigkhtGaXIKoGL60v8hTOT-a4u7OwZ_Y98jK8AlRcqQUcLjmtDHMCuY9i5am54h7XMQzgWSpQS5YusFJ5P5Nym2YqccghCf4EMeVtGcGemwKf_bOsXCqM86GK3r2hCSoDt3yAlp5v2UncAh6gQ1h3UF6YnA")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
# Send to multiple devices by passing a list of ids.
registration_ids = ["c48U7eFCyLQ:APA91bFSgMTzQOnMD7EbGdMrxTm_y9I4RTskWVSpsqyk2fhYg5POE6sS0Octb8xY2QHsyHtsy00EXIC26wdtji_XFRsY-bDAWfj-Ee_4CUh8DpV1mIvgJd55P7BCyXCncBl2t5FTZ0Nx"]
message_title = "Uber update"
message_body = "Hope you're having fun this weekend, don't forget to check today's news"
df = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title,
                                          message_body=message_body)


def got_result(result):
    print
    result


df.addBoth(got_result)
reactor.run()

# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAA3Mgl_0Y:APA91bFKigkhtGaXIKoGL60v8hTOT-a4u7OwZ_Y98jK8AlRcqQUcLjmtDHMCuY9i5am54h7XMQzgWSpQS5YusFJ5P5Nym2YqccghCf4EMeVtGcGemwKf_bOsXCqM86GK3r2hCSoDt3yAlp5v2UncAh6gQ1h3UF6YnA")

# OR initialize with proxies

proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "http://127.0.0.1",
        }
push_service = FCMNotification(api_key="AAAA3Mgl_0Y:APA91bFKigkhtGaXIKoGL60v8hTOT-a4u7OwZ_Y98jK8AlRcqQUcLjmtDHMCuY9i5am54h7XMQzgWSpQS5YusFJ5P5Nym2YqccghCf4EMeVtGcGemwKf_bOsXCqM86GK3r2hCSoDt3yAlp5v2UncAh6gQ1h3UF6YnA", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "c48U7eFCyLQ:APA91bFSgMTzQOnMD7EbGdMrxTm_y9I4RTskWVSpsqyk2fhYg5POE6sS0Octb8xY2QHsyHtsy00EXIC26wdtji_XFRsY-bDAWfj-Ee_4CUh8DpV1mIvgJd55P7BCyXCncBl2t5FTZ0Nx"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# Send to multiple devices by passing a list of ids.
registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
message_title = "Uber update"
message_body = "Hope you're having fun this weekend, don't forget to check today's news"
result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print result