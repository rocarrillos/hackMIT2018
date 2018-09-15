import requests

# We have to take in an audio file from where?

sample_audio_file = "https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3"
rodrigos_api_key = "01kGRVvJUBjR7uyXoDhAqKkR7J9ZKokRgt5WcZcs7mV9a98mfSZpqinis61H2aHzKBQiau23P4XovLIbrtEutS-UH1Bnc"

rev_headers = {
    "Authorization": "Bearer " + rodrigos_api_key
}


rev_payload = {
    "media_url": sample_audio_file
    "metadata":"This is a sample submit jobs option"}"
}

rev_reply = requests.post('https://api.rev.ai/revspeech/v1betatps', headers=rev_headers, data=rev_payload)
response_id = rev_reply["id"]

# curl -X GET "https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript" -H "Authorization: Bearer <api_key>" -H "Accept: application/vnd.rev.transcript.v1.0+json"

rev_data = requests.get("https://api.rev.ai/revspeech/v1beta/jobs/" + response_id + "/transcript", 
    headers={"Authorization": "Bearer " + rodrigos_api_key, "Accept": "application/vnd.rev.transcript.v1.0+json"})