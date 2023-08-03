# server.py
from flask import Flask, request
from google.cloud import storage
import json 

app = Flask(__name__)

service_account_key_json = r"""
{
  "type": "service_account",
  "project_id": "xobin-verification",
  "private_key_id": "18678b6bcd87914ea2b6b111322bd667fa855117",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDdoB2KVc+oEgp4\nwsUvxg0JAY1/Si+/1KKixxPKAzTT8GxVhII4Xd2C0eY8rO8LxcIfOMwls0FB8Hm7\n1Vaeis5wP3AuK5LiOvi2mQaFusK9Q1XpcmdlVScQhVMLW8REds5GwwCNcKBsKJbP\nRTruyHFeSOWbDQDdqlaoZPWe1I/qfUfus70z2j7Kx1KWMwhhNTxlQGr6e4t9Fv0E\nH1FC5Nqno3Bg4kW2cGJjwqZhM2mMIfiEB3arnuC+KGC/q0ztxADOLY/z1QUfAHus\nCxqZAF9gASBHNW86OpFW6EwA8AFmpTnsOBc7B2QVyxIQKma5/Mzr7QgkR6xIsWn2\nmiuPoj//AgMBAAECgf9fOm13A2g2z4mwWgBghrkTJZenGjlqM/Ot/dyC8N3CM4xZ\nMpbBoZOMoqRLbgNJC7Bdugn+KQfhTXMBQqn1da8+jAOn0xFKJAy6aQZkb9s9d7Fy\nnbXP1Mb0UlVcjBHJWUNJJIEYRUypLMegSB8KexY7bRc7iFrW5FpYAQmJNcyg9Gb9\nEw9A8tDz+O36t+W9q/aaYkc0DRtDN14aQ8YxV7jBZLwGWidD7zgVLd84sy1PrbAM\njNaE6qliexy1lwKATNTDfJe620yUiGWNxccDoN48t0m1PraqG4PbD61wBisIk+sg\nWdee6kMXMsJS1wC+S4DOYljLrlXfGU1YhcSxAIECgYEA+rDkGKltEo/yl7LsOoCJ\nWCuu7XPbedhxIEbTTR04cWLQGq2xfg5EpFyXkBn9dNKaDtfZDLurIKKmeo0PsFcn\n4E+2KHbmeOIDXiQr9wnIY2EKdEGLW8GDipLG6K0cAfrKy9PcSxXs78oS13Afxd+d\nOHirTO7gpZ3oXm3QyCueMSECgYEA4lGlo8bqrslJXejAG++jRVSwBXflKoNQnSk1\nB7ysnD2TW7VQ8nAcprcdOpUB1B3wpH0VE6q0fj4VsDpIe8tqexv7OsQIFIfaQpDJ\nbDOCuyUq+impGFY475Q+ZtIyAZ1RO5Vngbzw1gcoSbOX1QXl/PExFY3GI6LK9+Gh\njxxnrR8CgYABWayQ2XDF9dKHsKYHFqQmvm19x+75tAm/88G1m5+vNKoMSr03AZqr\nC/ihBRLRa0T7KXx4zhX44gdlh5b7Cy0izysbArDxG76K5kT6WqoipuYohCXdA6jS\nuUGrBSuucwxelrCMEv0ouXzqficdqLuvDy9VBcBeBAC5aXwDaAC9IQKBgQDNKRqw\n9xezzwDVQrM0H+6wYO8YZfG2skeX0M0j8GPBVwiIcDurKvquHv0+J+n6chG96y36\nIBty/bEHii4/Gs2yQFFkmmSAyA6RnVMa5S8zm6P0F2QUjcUbWhWffBic4hHLo8qr\nD657Nw3MkiOnlqtAuxy130mo8GByiXW9mBBcHQKBgQC43SNiMHwaIEmoKl94VWJm\nyrniccaFfHVipt7gdrEFj7U/ReV44Lvzs68eU559j+3FtaLmm0vnlSLoUiKtxRao\n/AubE9g0OczZFVUUYQxavRLJ3Pn2Tu4xD3ROKMOecD/LMGMIRkHixsupSHLulhgw\nseoMMLLxBNCu3wWYmM67nA==\n-----END PRIVATE KEY-----\n",
  "client_email": "manas-app-engine@xobin-verification.iam.gserviceaccount.com",
  "client_id": "107808672898467037078",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/manas-app-engine%40xobin-verification.iam.gserviceaccount.com"
}
"""


service_account_key = json.loads(service_account_key_json)

# Create a storage client using the service account key
storage_client = storage.Client.from_service_account_info(service_account_key)

bucket_name = 'live-streaming-storage-manas'
bucket = storage_client.bucket(bucket_name)

@app.route('/upload', methods=['POST'])
def upload_chunk():
    chunk = request.files['chunk']
    filename = request.form['filename']

    blob = bucket.blob(filename)

    if not blob.exists():
        print("Blob does not exists")
        blob.upload_from_file(chunk)
    else:
        print("Blob exists")
        with blob.open('wb') as file:
            file.write(chunk.read())

    return 'Chunk uploaded successfully'

if __name__ == '__main__':
    app.run()
