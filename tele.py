import telebot

chave = "6028892799:AAFiKNAdqTzqcRHXcqdoPlykDx1k255fTaU"
chat_id = "1427119084"

bot = telebot.TeleBot(chave)


@bot.message_handler(commands=["start"])
def responder(inicio):
    bot.send_photo(inicio.from_user.id,
                   photo="https://scontent-for1-1.xx.fbcdn.net/v/t39.30808-6/402106565_907740337440208_6687529766115017951_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGHgnQIupxFBNmxHjvx3JmA7AZIGqr8SJXsBkgaqvxIlSntaP6C6YAjdV-68Va-rjfMho7fac1teUK1Sj8_rGaW&_nc_ohc=BK-qeocueMEAX9oEc0O&_nc_ht=scontent-for1-1.xx&oh=00_AfBSGj__F4h0I8P7BV9jBrJbKwrgp5yAq4smbQegkfHCTg&oe=65621DB7",
                   caption="Ola! Somos a loja Murilo Gomes, temos como objetivo vender cursos!. Digite /cursos para os nossos cursos ou /empresa para conhecer nossa empresa.")


@bot.message_handler(commands=["cursos"])
def opcoes(mensagem):
    texto = """
    Escolha a área de seu curso:
    /Marketing
    /DesingWeb
    /Culinaria
    /Gari
    /Yoga"""

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["empresa"])
def opcoes(mensagem):
    texto = """
    Opções para conhecer nossa empresa:
    /quemsomosnos
    /murilo"""

    bot.send_message(mensagem.chat.id, texto)


# ESCOLHA DOS CURSOS

@bot.message_handler(commands=["Marketing"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/404349242_122130462332067537_5729683003648836414_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHoou6eBWxY7t0_UgCmnkWrRp3wbhiy5QBGnfBuGLLlAGUo2gxrKuv08sHnohnRfuNaBvsrs3CJgRUT0dFnGZ0M&_nc_ohc=RHBi6B36vAcAX-m94sW&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfB9D5pj3u75C2mpIhxTzObK3Ttn97d7G5AsF36_KyYkVA&oe=6561ADA2",
                   caption="O curso de Marketing abrange estratégias para promover produtos ou serviços, desde análise de mercado até a implementação de campanhas publicitárias eficazes. Os participantes aprenderão sobre branding, mídias sociais, análise de dados e técnicas de publicidade. Assine o nosso curso: /CompraMarketing")


@bot.message_handler(commands=["DesingWeb"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/403682042_122130462194067537_7176114956553679934_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHWKZ01oKjJ4oTvmDKCMiQNJN0CGwE9Losk3QIbAT0uiyTpDy0wbs-i7oQ9mOer3aN6K2iHL3vkNbDEaQEmp8Pr&_nc_ohc=WzA62uUBBwQAX8FZsMP&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfCD9y-zWQyizIg_n2-UOokc0dnsbk99AeckAUZIisoRkQ&oe=6561986F",
                   caption="Este curso oferece conhecimentos práticos e teóricos sobre design web, abrangendo desde princípios de design até habilidades técnicas como HTML, CSS e design responsivo. Os alunos aprenderão a criar interfaces atraentes e funcionais para sites modernos. Assine o nosso curso: /CompraDesingWeb")


@bot.message_handler(commands=["Gari"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/404373869_122130462380067537_1224380065145938493_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHoqKEvZzksM9P_cAPnj70zDL2HsVOAJkIMvYexU4AmQo_XmmI3-74_hYsVGdym-vM-qwurXhXmbqdwc0_TsEPT&_nc_ohc=Jku65upCH7oAX8pYDXA&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfBHrc69q9Q7SZQJnCqRH7pKiC1CJ590jsjiUNhCmIfC2A&oe=65613D1C",
                   caption="Este curso aborda a importância da coleta de resíduos, destacando práticas sustentáveis e métodos eficientes de gestão de resíduos. Os participantes aprenderão sobre a segurança e as melhores práticas associadas à profissão de gari, contribuindo para um ambiente mais limpo e saudável. Assine o nosso curso: /CompraGari")


@bot.message_handler(commands=["Culinaria"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/402143286_122130462272067537_3397677700799831651_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFUqdqx2yRuo-Ch6U8qfA-jzgNw6V5BzVnOA3DpXkHNWQBKfOf9I8s57LGMYk0DqTebfK5xGsdGR7AhQvcab0dm&_nc_ohc=F7albXqD9WAAX_NQ4Pl&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfD9rpqmXVk01x9cXOreOvjUX7xMmqSBThHpe-3TmOkB1A&oe=656272D2",
                   caption="O curso de Culinária é ideal para entusiastas gastronômicos e aspirantes a chefs. Ele cobre técnicas culinárias básicas, apresentação de pratos, seleção de ingredientes e até mesmo noções de gestão de cozinha. Os participantes desenvolverão habilidades práticas na arte da culinária. Assine o nosso curso: /CompraCulinaria")


@bot.message_handler(commands=["Yoga"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/403604936_122130462428067537_6615021984035286440_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFnBOjExBXnz-vEiNmhASAJNXmhatPUa4g1eaFq09RriBoD6Xbcc1iRxRM4dXt1OC8KV3GX62Lwk74uXwe6WzPY&_nc_ohc=kOz3dwv7G2IAX-T8LXx&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfCiWgruA75Uib4McFKTooT-7yUyY_bR9yzt43ANOMOlLw&oe=65623CC4",
                   caption="O curso de Yoga proporciona uma introdução abrangente à prática milenar do yoga. Ele engloba posturas (asanas), técnicas de respiração (pranayama) e meditação, visando promover o equilíbrio físico e mental. Os participantes aprenderão a incorporar o yoga em sua vida cotidiana para melhorar o bem-estar. Assine o nosso curso: /CompraYoga")


@bot.message_handler(commands=["quemsomosnos"])
def opcao(mensagem):
    bot.send_photo(mensagem.from_user.id,
                   
                   photo="https://scontent-for1-1.xx.fbcdn.net/v/t39.30808-6/402106565_907740337440208_6687529766115017951_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGHgnQIupxFBNmxHjvx3JmA7AZIGqr8SJXsBkgaqvxIlSntaP6C6YAjdV-68Va-rjfMho7fac1teUK1Sj8_rGaW&_nc_ohc=BK-qeocueMEAX9oEc0O&_nc_ht=scontent-for1-1.xx&oh=00_AfBSGj__F4h0I8P7BV9jBrJbKwrgp5yAq4smbQegkfHCTg&oe=65621DB7",
                   caption="Seja bem-vindo à Murilo Gomes, sua porta de entrada para um universo de aprendizado e crescimento pessoal e profissional. Aqui, acreditamos que o conhecimento é a chave para o sucesso, e estamos empenhados em fornecer cursos de alta qualidade que capacitam indivíduos a alcançarem seus objetivos e sonhos.")

@bot.message_handler(commands=["murilo"])
def opcao(menssgem):
        bot.send_audio(menssgem.from_user.id, audio=open("murilo.m4a", 'rb',), caption="Até onde chega o meu conhecimento, Murilo Gomes não é uma divindade ou uma figura religiosa reconhecida globalmente. Parece ser um nome comum de pessoa. Se Murilo Gomes é um deus em algum contexto específico ou cultura local, eu não tenho informações sobre isso. Se você puder fornecer mais contexto ou informações sobre a divindade Murilo Gomes, eu ficarei feliz em tentar ajudar da melhor maneira possível!")
        bot.send_photo(menssgem.from_user.id, photo="")

@bot.message_handler(commands=["CompraMarketing"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Compra aqui: https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiz86f66NeCAxV6YkgAHRpeBfUYABAAGgJjZQ&ae=2&gclid=Cj0KCQiA6vaqBhCbARIsACF9M6l16kuNkLuSpVq9PgS7SfXsypTd1HAsbMB1dgWN7E4pDU1aJSXwMxgaArqjEALw_wcB&ohost=www.google.com&cid=CAESVuD2TrElanY2TfffG-KGij7gtyPXGciH8kdZGYZJrArubcfSYKtCuw_PO3YrFyQcZMM5KSgw04ZEN3hFUJWMPiEqvaeLK1oTaWjBc3gIK0LWr1qY1fIf&sig=AOD64_3q1fXgsEgPuXPMwFG0Lbv9J7uOwA&q&adurl&ved=2ahUKEwiC4J_66NeCAxV6qJUCHdUfD44Q0Qx6BAgMEAE")

@bot.message_handler(commands=["CompraCulinaria"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Compra aqui: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjT6eqI6deCAxUKlJUCHVkNCEAQFnoECAkQAQ&url=https%3A%2F%2Fwww.iped.com.br%2Fculinaria-gastronomia&usg=AOvVaw2SanjoMezzx-cP565T9-2X&opi=89978449 ")

@bot.message_handler(commands=["CompraDesingWeb"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Compra aqui: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjMydKc6deCAxWIpZUCHcT5CS4QFnoECB8QAQ&url=https%3A%2F%2Fwww.udemy.com%2Fpt%2Ftopic%2Fweb-design%2F&usg=AOvVaw1dJCKo58H84f5ujTzQPUI2&opi=89978449 ")

@bot.message_handler(commands=["CompraGari"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Compra aqui: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiKhKep6deCAxVwr5UCHec4DxgQFnoECAgQAQ&url=https%3A%2F%2Fwww.wreducacional.com.br%2Fcurso-de-gari&usg=AOvVaw17e4aI9KLU3VfqCO2wF1Fu&opi=89978449 ")

@bot.message_handler(commands=["CompraYoga"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Compra aqui: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjYtdmz6deCAxXtq5UCHY7uBF8QFnoECBAQAQ&url=https%3A%2F%2Fnamu.com.br%2Fcategoria%2Fyoga%2F&usg=AOvVaw3OozwKDt1r01sqyjj1-6z5&opi=89978449 ")

#ENVIO DE AUDIO

@bot.message_handler(commands=["Gari"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/404373869_122130462380067537_1224380065145938493_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHoqKEvZzksM9P_cAPnj70zDL2HsVOAJkIMvYexU4AmQo_XmmI3-74_hYsVGdym-vM-qwurXhXmbqdwc0_TsEPT&_nc_ohc=Jku65upCH7oAX8pYDXA&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfBHrc69q9Q7SZQJnCqRH7pKiC1CJ590jsjiUNhCmIfC2A&oe=65613D1C",
                   caption="Este curso aborda a importância da coleta de resíduos, destacando práticas sustentáveis e métodos eficientes de gestão de resíduos. Os participantes aprenderão sobre a segurança e as melhores práticas associadas à profissão de gari, contribuindo para um ambiente mais limpo e saudável. Assine o nosso curso: /CompraGari")

#@bot.message_handler(commands=["murilo"])
    #def opcao(menssgem):
            #bot.send_audio(menssgem.from_user.id, audio=open("murilo.m4a", 'rb'))

bot.polling()



