#!/usr/bin/env python3
"""Fetch generated Mila voice recordings only if the 29 permanent MP3 files are missing.
This bootstrap file contains TEMPORARY signed links; once audio files are committed,
remove this script and its workflow invocation if you want to remove expiring links.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import sys, json, time
ROOT=Path(__file__).resolve().parent.parent
LINKS=[
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/fc2e86be-638b-4b91-907e-7213f1d16a19/Mila13_Final_Szene_01.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiN2I0ZTY2Zjg2Mzg5M2E2YyIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI1NTczNn0.knsC5NH3OIszhnCwwccpPNG3O4ghT2vTUxAIQuGvp0E",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/318f0016-0a91-49bb-b790-b9e7b4a4522b/Mila13_Final_Szene_02.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiZjgzZTliOGNjYmI1MmUzYSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIyMjIyMH0.HgrEzv_TEDBNCxwvry668MLOiU0dhvomQuQMXY07wcg",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/eda77dfa-8df3-4b67-bd71-beb99a3b8f53/Mila13_Final_Szene_03.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMjQ2OTJmZDkxYTVkMWQyZSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIyMDUwNX0.h5Bpx8cQDURN15rS-F6I9jBXKvXo9p_39PkZ0_oV5JU",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/5f616f1f-0116-4044-945b-214029d85f33/Mila13_Final_Szene_04.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMDc1MThlODUzMjJlMTc1ZCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIwNjIxM30.oErjyRb-EHsZmgsqsbPfDT0gQeeoWBYnwS51ryfdIQ8",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/439984e5-5015-4380-9f9e-66d206872da6/Mila13_Final_Szene_05.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNjg1MzI1YzU4N2RhM2VmMiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjE4MzYyMX0.riut1a6BrNLSIyacQx87MmSQHJPtcAFa52-ANRlGLts",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/084b1fbe-9acd-4bd0-ad43-ced273225ec6/Mila13_Final_Szene_06.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiOWE3MTc5OGM3OTkxYzM1OCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjE4NzE0OH0.hZKIYbWKPpJW3urXmlQl00eoxCiw822VFWmP5PX3sHM",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/cbdda844-6ad2-4f58-9736-e9ac0d414e14/Mila13_Final_Szene_07.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNjVjOTJiZTA1ODQ0YTc5ZCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjE4MTk4NH0.-TVDD6n_dHos1_P9MAAw3CWCCUqLdPHhiwtn-PvFZz0",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/c42af53d-78b1-44da-9bd1-74d5cb7835c7/Mila13_Final_Szene_08.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiN2JkYTJjMGE3MDI4Y2ZhZiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI1NzI5MH0.Y5uAmArgwQTWJZfOt3dsScMAYXV19H0Fw0pJwD_MATA",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/63852d95-c032-4d30-82a7-4e2f126099d6/Mila13_Final_Szene_09.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNWY4NDA4YzZmMzczYzY3ZiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIyMjkxOH0.6p-47GBDilB1IxaQ2Rq8XF4UurKKN8hfsoyZzh48pvI",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/67b80eea-756e-4c99-a8af-2086a1cb6d4d/Mila13_Final_Szene_10.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMzA4ZTUxZjgwNTgwYTFjMyIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI0OTQ2NH0.f7WeKwr1O_7GQnTZoBTpGA2O1AVks6R6nAJRa2FSBSo",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/1046bd4c-bc72-4d90-95c9-9273b70d2532/Mila13_Szene_11.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiOTJjNzkyMGE3M2E5N2EzNiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI2MTM4Nn0.PM3TTdSRei0OXJ0KS9gkJd1pv0wXSRY0__d-4HJxyIk",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/4d9d55ed-1aad-4842-85be-d3191f6df5dd/Mila13_Szene_12.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiODAwZjM3YTk0NjFjZDc3ZSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI1MzczN30.mhYRE2UTtYZBiu9kvaFYIRHHOZVUZ7txDJ3KWoEAulg",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/5b527c0f-188e-4843-a770-1967da1d058c/Mila13_Szene_13.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNGZmMWNjMjY2Y2ZkYTMzNyIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI1NDUwMn0.9siYoGSxyVKgWUfHt5RKs2tlCw7AHdKgIN3w8Eky-JI",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/494f6a8a-103d-4108-8f0d-cd8183026df2/Mila13_Szene_14.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMmNjMjY2YzJlMjhhNGM3NiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIzMDU5NH0.UZWhMFPuaFpDtTmjfQRk1aNnekWcegK-n5Az0GNYc4Q",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/25d7c5b1-8595-438b-9ac6-2456f312c6b9/Mila13_Szene_15.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiM2Y4OWJmMzE2NmExODllMSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjE4Mzk4NX0.AZtRsz3pOnYxSCR_edSwemjTGNqmmNcTNRKim0mcSZE",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/60c7cf71-1c34-46ca-899d-84f3d4d510f4/Mila13_Szene_16.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiZDQyNGMwZTVkNTFjM2MyOCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIxMjA2OX0.Zzv4nL7r4p-m-M_KKi2LkKzb_sOiob8oXXRVA1vpAhM",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/a00940cd-aab3-4170-9f15-b649c7d9d639/Mila13_Szene_17.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiOTk2MDdhYjI3ODQ4ZDU2MiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjE4MDkxNH0.ygD7Wy1GYP0TRB99wQM9tuDH4oAott-hes_rgH4R6gY",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/5b261f33-dcfb-4ee0-afe5-078e12f8a52e/Mila13_Szene_18.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiYmJiNzE2NzE2YTE4MjhkZCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI1MzQyNX0.xsz90QsXo-01N3LRRZfaGmP9wuzOOyCOmV2BuG-PGlA",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/a15970c8-aa4d-408b-8313-245c95fed419/Mila13_Szene_19.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiZDljOWJiZGQxOGNhNGZiNiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIxNTkwMX0.AkrolsGG2FZMXoQ5IxB03ls866TX1WYsOWBRvXuuYmk",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/cce9f6b2-f02e-425d-927d-c3df7a7f13dc/Mila13_Szene_20.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMDk0ZmZkNjk4NzIxODIwMCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIyMTE2MX0.wNLJF7eSI1-bQjeUGvUD-j9tR-k6IBh8UgVU9EGI90Q",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/07b543a7-ff73-4947-a590-0732769dade6/Mila13_Szene_21.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiN2E0YmM4N2I0ZjA4NGRjNiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI0MTI3NX0.XYrVGpdpVm3FCH4J5K2QDYuwLrjT0wgczotX6LCbriY",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/ebd00d63-d9fa-42ae-8cc4-4061d148ba49/Mila13_Szene_22.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiOTUyZWE0NzExNGE4YjI2NyIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIyMTkzN30.6NJ3DZHr7eEW6ebbdSDwhfcSYv9RSKKz1YJShG23KtI",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/2019785d-1ec7-4b43-b49f-bf1c355bd3ae/Mila13_Szene_23.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNTQ0ZjM5ZjkyZGE4NzJiZCIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIxOTEyOX0.qnXvf4h6ne9nslRjWfJ5pCWLifZ5nnJFuQDG7aOkXN8",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/659b8284-eed0-4d7b-9238-3e73d8538d9a/Mila13_Szene_24.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiY2ZkZDE2ZjA5ZDM2ODcxYiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIwNTA0MH0.rUfIYR6UiqWkOO0-rSIKJD5Sj3bwsgiFIEd0JDGjqFo",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/12c6d0a4-6d4e-4593-9508-c9594ab8df8c/Mila13_Szene_25.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiZjk3NmRiN2IxYzE0YmUwNiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIwOTAxOX0.76X3LNa-wjLt5k5miT3x7FsZCHPOKQFS5Gvyx4Dfgxo",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/7bcb7b89-bfb5-49f4-a5a0-f334e605951d/Mila13_Szene_26.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNDBkNmM1MmMyMjQ2ODBlNyIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIzNjIwNH0.p55IUaOGlYpb3kf19nuXhoXGYi9wj74-KQgr1Vs_bJk",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/2ff89db3-78a7-4bb9-9370-188ea439c683/Mila13_Szene_27.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMDhlYWJjYzE0NThlNTA2YiIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjIzODI3M30.aglTIh9xnWrmiPzqSF3dYefGxdwpO2FOL880us4wlw4",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/8c96e688-f401-4468-aa2f-98de9ea7de45/Mila13_Szene_28.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNGZmNzJjZTNkZjQwMDI4OSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjI2MTM0N30.1HBmB3gLMTbOI8fTkrWmI_MhzffCCRW2WKFoOBo9lFU",
  "https://dnznrvs05pmza.cloudfront.net/text_to_speech/0c77b60c-3247-461c-a1a5-02dbd28f92d1/Mila13_Szene_29.mp3?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNDcxNjg0NmFlMzc0NjQxYSIsImJ1Y2tldCI6InJ1bndheS10YXNrLWFydGlmYWN0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5MjE4NzYyNn0.w7lD6BXY7vdfeEG3uJh-ysBVjs-XCn7d1FXzKkDw_rg"
]
assert len(LINKS)==29
missing=[]
for i,url in enumerate(LINKS,1):
    p=ROOT/'audio'/f'{i:02d}.mp3'
    if p.is_file() and p.stat().st_size>5000:
        print(f'✔ {p.name} ({p.stat().st_size} Bytes already present)',flush=True)
        continue
    missing.append(i)
    for attempt in range(3):
        try:
            print(f'Downloading {i:02d}/29 (attempt {attempt+1}) ...',flush=True)
            with urlopen(Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=45) as r:
                data=r.read()
            if len(data)<5000 or not (data.startswith(b'ID3') or data[:1]==b'\xff'):
                raise ValueError(f'Unexpected mp3 payload ({len(data)} bytes)')
            p.parent.mkdir(exist_ok=True)
            p.write_bytes(data)
            break
        except Exception as e:
            print(f'Failed: {e}',file=sys.stderr,flush=True)
            if attempt==2:raise
            time.sleep(3)
final=list((ROOT/'audio').glob('??.mp3'))
if len(final)!=29:raise RuntimeError(f'Only {len(final)}/29 MP3 files present.')
print(f'All 29 MP3 files saved for permanent hosting; newly downloaded: {len(missing)}',flush=True)
