import requests

url = 'https://api.zenvia.com/v2/channels/sms/messages'

session_requests = requests.session()

heards = {
        'Content-Type: application/json' 
        'X-API-TOKEN:l5ykz70UKXOWmuVQxLxfBe2RHAzTJ4jZSY9b'
}

values = """{
	"from":"garrulous-honesty",
	"to":"559791388065", "559288192972", "559293290162","contents":[{
	"type":"text",
    "text": "Assunto: DESAFIO TALENT LAB ITACOATIARA",
    "text":"Olá, meu nome é Marlon Deivid Lopes da Silva  e estou participando do “PROGRAMA DE ESTÁGIO TALENT LAB ITACOATIARA (Nível Superior)"}]
}"""

result = session_requests.post(
    url, 
    data = values,
    headers = dict(referer = url)
)

			