lista_perguntas = [
    {
        'pergunta': 'O que é mais pesado: 1 quilo de algodão ou 1 quilo de ferro?', 
        'resposta': 'Ambos', 
        'alternativa1': 'Nenhum deles', 
        'alternativa2': 'Ambos', 
        'alternativa3': 'Ferro', 
        'alternativa4': 'Algodão', 
        'alternativa5': ''},
    {
        'pergunta': 'Quem inventou a lâmpada?', 
        'resposta': 'Thomas Edison', 
        'alternativa1': 'Graham Bell', 
        'alternativa2': 'Steve Jobs', 
        'alternativa3': 'Thomas Edison', 
        'alternativa4': 'Henry Ford', 
        'alternativa5': 'Santos Dumont'},
    {
        'pergunta':'Qual o melhor anime de todos os tempos' ,'resposta': 'One Piece', 
        'alternativa1': 'One Piece', 
        'alternativa2': 'Naruto', 
        'alternativa3': 'Fairy Tail', 
        'alternativa4': 'Dragon Ball', 
        'alternativa5': 'Bleach'},
    
    {
        'pergunta': 'Quanto tempo a Terra demora para dar uma volta completa em torno dela mesma?', 
        'resposta': '24 horas', 
        'alternativa1': '24 horas', 
        'alternativa2': '365 dias', 
        'alternativa3': '7 dias', 
        'alternativa4': '365 ou 366 dias', 
        'alternativa5': '30 ou 31 dias'},
    {
        'pergunta': 'A que temperatura a água ferve?', 
        'resposta': '100 ºC', 
        'alternativa1': '200 ºC', 
        'alternativa2': '-10 ºC', 
        'alternativa3': '180 ºC', 
        'alternativa4': '0 ºC', 
        'alternativa5': '100 ºC'},
    {
        'pergunta':'Quem foi a primeira pessoa a viajar no Espaço?' ,
        'resposta': 'Yuri Gagarin', 
        'alternativa1':'Yuri Gagarin',
        'alternativa2':'A cadela Laika',
        'alternativa3':'Neil Armstrong',
        'alternativa4':'Marcos Pontes',
        'alternativa5':'Buzz Aldrin'},
    {
        'pergunta':'Qual a montanha mais alta do mundo?' ,'resposta': 'Monte Everest', 
        'alternativa1':'Mauna Kea',
        'alternativa2':'Dhaulagiri',
        'alternativa3':'Monte Chimborazo',
        'alternativa4':'Monte Everest',
        'alternativa5':'Pico da Neblina'},
    {
        'pergunta':'Onde se localiza Machu Picchu?' ,'resposta': 'Peru', 
        'alternativa1':'Colômbia',
        'alternativa2':'Peru',
        'alternativa3':'China',
        'alternativa4':'Bolívia',
        'alternativa5':'Índia'},
    {
        'pergunta':'Que país tem o formato de uma bota?' ,'resposta': 'Itália', 
        'alternativa1':'Butão',
        'alternativa2':'Brasil',
        'alternativa3':'Portugal',
        'alternativa4':'Itália',
        'alternativa5':'México'},
]

lista_palavras = [
    {'palavra':'carro','dica1':'um veiculo de quatro rodas'},
    {'palavra':'helicoptero','dica1':'Não Possui Asas Mas Voa'},
    {'palavra':'relogio','dica1':'usado para marcar o tempo'},
    {'palavra':'maça','dica1':'uma fruta vermelha'},
    {'palavra':'coach','dica1':'profissão inutil'},
    {'palavra':'cachorro','dica1':'o melhor amigo do homen'},
    {'palavra':'gato','dica1':'dono da raça humana'},
    {'palavra':'hamster','dica1':'hamtaro, são alegres e fofinhos'},
    {'palavra':'ampulheta','dica1':'quanto mais parado fico, mais rapido corro.'},

]


if __name__ == '__main__':
    import os, django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    django.setup()

    from perguntas.models import Pergunta
    from forca.models import Palavra

    def gerando_perguntas():
        for pergunta in lista_perguntas:
            questao = pergunta['pergunta']
            resposta = pergunta['resposta']
            alternativa1 = pergunta['alternativa1']
            alternativa2 = pergunta['alternativa2']
            alternativa3 = pergunta['alternativa3']
            alternativa4 = pergunta['alternativa4']
            alternativa5 = pergunta['alternativa5']
            pergunta = Pergunta(pergunta=questao,resposta=resposta,
            alternativa1=alternativa1,
            alternativa2=alternativa2,
            alternativa3=alternativa3,
            alternativa4=alternativa4,
            alternativa5=alternativa5
            )
            pergunta.save()

    def gerando_palavras():

        for palavra in lista_palavras:
            questao = palavra['palavra']
            dica = palavra['dica1']
            forca = Palavra(palavra=questao,dica1=dica)
            forca.save()

    gerando_perguntas()
    print('Perguntas Geradas ')
    gerando_palavras()
    print('Palavras Geradas ')
    