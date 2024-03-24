from openai import OpenAI
import credentials

client = OpenAI(api_key = credentials.api_key)


def chat(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",)
    return(chat_completion.choices[0].message.content)



def povzetek(okroznice, st):
    odgovor = "Prosim napiši mi povzetek teh okrožnic: "
    a = 0
    for okroznica in okroznice:
        a = a + 1
        okroznica = okroznica.replace("Lep pozdrav,Andrej SmrduGimnazija Vi=C4=8DSporo=C4=8Dilo je bilo poslano preko sistema SOLSIS.", "")
        okroznica = okroznica.replace("=C4=8D" , "č")
        okroznica = okroznica.replace("=C4=8C", "Č")
        okroznica = okroznica.replace("=C5=A1" , "š")
        okroznica = okroznica.replace("=C5=A0" , "Š")
        okroznica = okroznica.replace("=C5=BE", "ž")
        okroznica = okroznica.replace("=C5=BD", "Ž")
        odgovor = odgovor + okroznica + "       "
        if st == a:
            break
    koncni = chat(odgovor)
    return(koncni)