import requests
import time


sample_audio_file = "https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3"


class RevAPICall:
    """Class for interaction between Python and the Revspeech API."""
    def __init__(self):
        self.sample_audio_file = "https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3"
        self.api_key = "01etgfFEQMLBxmOKPKLcraotL233SwQBow3yzH40jId0Sz6K8q_o9DfzUwjJ908oJYj1xEIsd0rlxNAIVO3SxiL7AAqvQ"
        self.rev_headers = {"Authorization": "Bearer " + self.api_key, "Content-Type": "application/json"}

    def query_rev(self, job_id):
        """Helper function for querying Revspeech for the response. Users should not need to use this function."""
        try:
            if self.get_response(job_id).json().get("current_value") == "in_progress":
                print("waiting")
                time.sleep(2)
                return self.query_rev(job_id)
            else:
                return self.get_response(job_id).text
        except:
            return self.get_response(job_id).text

    def get_response(self, job_id):
        """Helper function for querying Revspeech for the response. Users should not need to use this function."""
        return requests.get("https://api.rev.ai/revspeech/v1beta/jobs/%s/transcript"% job_id, 
            headers={"Authorization": "Bearer " + self.api_key, 
            "Accept": "text/plain"})
    
    def transcribe(self, filename):
        """Function for transcribing an audio file into text. 
        Arguments: 
            filename: the path to the file to be transcribed
        Returns:
            transcription of file as plaintext
        """
        rev_data = "{\"media_url\":\"%s\",\"metadata\":\"This is a sample submit jobs option\"}"% filename
        rev_reply = requests.post('https://api.rev.ai/revspeech/v1beta/jobs', 
            headers=self.rev_headers, data=rev_data)
        response_id = rev_reply.json().get("id")
        response_data = self.query_rev(response_id)
        return response_data