#Çalışmıyor
from openai import OpenAI

client=OpenAI(api_key="OPEN AI API")

messages=[{"role":"user","content":""}]

while True:
    prompt=input("Bir prompt giriniz:(çıkış  için q 'ya basınız)")
    if prompt=="q"or prompt=="Q":
        break
    else:
        completion=client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role':'user','content':prompt}]

        )

        print(completion.choices[0].message)
        messages.append=({'role':'asistant','content':completion.choices[0].message})