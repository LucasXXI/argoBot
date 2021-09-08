from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('ArgoBot', logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation'],)

conversa = ChatterBotCorpusTrainer(bot)
conversa.train('chatterbot.corpus.portuguese.greetings',
               'chatterbot.corpus.portuguese.linguistic_knowledge',
               'chatterbot.corpus.portuguese.conversations',)


chat = ListTrainer(bot)
chat.train([
    'oi',
    'Opa,tudo bem?',
    'Qual seu nome?',
    'Sou ArgoBot, estou aqui pra ajuda-lo no CESUPA! ',
    'prazer em te conhecer',
    'igualmente, meu patrão',
    'gostaria de saber sobre o as salas',
    '1 andar: salas 1 a 7\n2 andar: Secretaria e Biblioteca\n3 Andar: Salas de 8 a 15\n4 andar: Salas de 15 a 21 e Auditório',
    'Qual meu login?',
    'Para fazer seu primeiro acesso, utilize número de matrícula como login  e sua senha será sua data de nascimento no formato DD/MM/AA',
    'obrigado',
    'Não há de que! Engenheiro ajuda engenheiro',
])

while True:
    try:
        response = bot.get_response(input("usuário: ").lower())
        if float(response.confidence) > 0.2:
                print("ArgoBot: ", response)
        else:
            print("ArgoBot: Não entendi")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break