import telebot

chave = "6028892799:AAFiKNAdqTzqcRHXcqdoPlykDx1k255fTaU"
chat_id = "1427119084"

bot = telebot.TeleBot(chave)


# INICIO

@bot.message_handler(commands=["start"])
def responder(inicio):
    bot.send_photo(inicio.from_user.id,
               photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/405230220_122132232158067537_249974436057333749_n.jpg?stp=dst-jpg_p843x403&_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGhujRk3kqTU97wLzHaqlAKjsoLW98ZWBKOygtb3xlYEklAPbH6Hgt541-znrgh4hgpzywyli5C8kSpObQhi5tZ&_nc_ohc=LDBuxRcEsyUAX8vel4z&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfAmlv6C5P1bL17ajzOo8DYiYEtJRYiVTHCS5ONk5z52Sg&oe=656AC5C4",
               caption="Olá! Somos a escola EEEP Paulo Petrola, temos como objetivo com esse bot, mostrar um pouco mais sobre cada curso do PP!. Digite ou clique em /cursos para os nossos cursos ou /escola para conhecer nossa escola.")


@bot.message_handler(commands=["cursos"])
def opcoes(mensagem):
    texto = """
    Escolha a área de seu curso:
    /Guia
    /Enfermagem
    /Informatica"""

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["escola"])
def opcoes(mensagem):
    texto = """
    Opções para conhecer nossa escola:
    /quemsomosnos
    /PP"""

    bot.send_message(mensagem.chat.id, texto)


# ESCOLHA DOS CURSOS

@bot.message_handler(commands=["Guia"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent-for1-1.xx.fbcdn.net/v/t39.30808-6/405316493_911286583752250_6503235167382143602_n.jpg?stp=dst-jpg_p600x600&_nc_cat=102&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHl_-09DC5g23jfcSzdbrdKIdX5RzpfOZQh1flHOl85lNh7RU2PWUub_MTyO8Hnz8mb5Pd4PlZ0zLrcsp6FjYWx&_nc_ohc=sO3jBWM_qg8AX_M3W8b&_nc_ht=scontent-for1-1.xx&oh=00_AfD8YRLXkAFybRwcoIKeJeoDSlm-x-RerKGEcnlDHGHdKg&oe=656A7101",
                   caption="O curso de Guia de Turismo na Escola Profissionalizante Paulo Petrola oferece uma formação abrangente para aqueles interessados em explorar a indústria do turismo. Guiados por profissionais experientes, os alunos adquirem conhecimentos práticos e teóricos, desde destinos turísticos até técnicas de comunicação. Com um enfoque prático, o programa inclui experiências em campo e destaca-se por preparar os alunos para liderar grupos e oferecer informações relevantes aos visitantes. Ao concluir o curso, os estudantes estarão capacitados para uma carreira dinâmica como guias de turismo, atendendo às crescentes demandas desse setor. Clique em /sobreguia para mais.")


@bot.message_handler(commands=["Enfermagem"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent-for1-1.xx.fbcdn.net/v/t39.30808-6/406387486_911286573752251_2859501334240123270_n.jpg?stp=dst-jpg_p600x600&_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFrfCCMYa47fmQ69uGCrUminQls5f1qnf-dCWzl_Wqd_5iiEYvqAZJgv9LSJo9PCIwxpFCvxNwPM9EWjtC0GTl3&_nc_ohc=h_dq1dE6uPsAX9ak6DQ&_nc_ht=scontent-for1-1.xx&oh=00_AfCqphQ7HBPCxk0rCfEoKh-Uith3KsRev2jbxrv3cslPwg&oe=6569FA29",
                   caption="O curso de Enfermagem na Escola Profissionalizante Paulo Petrola oferece uma sólida formação para quem busca se dedicar à área da saúde. Sob orientação de profissionais experientes, os alunos exploram teoria e prática, preparando-se para atuar em diversos contextos de cuidados. Com laboratórios bem equipados, o curso proporciona uma jornada prática e enriquecedora, preparando os estudantes para uma carreira gratificante na enfermagem. Clique em /sobreenfer para mais.")


@bot.message_handler(commands=["Informatica"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent-for1-1.xx.fbcdn.net/v/t39.30808-6/405363130_911286540418921_3716957910338018699_n.jpg?stp=dst-jpg_p600x600&_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHdTqrjdlMj0uzP1djfMy6h4bkA51KHD2fhuQDnUocPZ31AxyNxwQ_ESyIOkgPHt06CIPx391SlxAWHL7DOaxAo&_nc_ohc=TDzenyFxjAcAX8xJp6m&_nc_ht=scontent-for1-1.xx&oh=00_AfBfMLbo7Bq_GEMnPxWF-WRBqe8a1LheS2T9g5BCmlAB_w&oe=656AB2E5",
                   caption="O curso de informática na Escola Profissionalizante Paulo Petrola oferece uma sólida formação para iniciantes e aprimoramento para quem busca aprofundar seus conhecimentos. Ministrado por instrutores qualificados, abrange desde fundamentos de hardware e software até programação e redes de computadores. Com foco prático e laboratórios equipados, os alunos desenvolvem habilidades prontas para o mercado de trabalho. Ao concluir o curso, estarão preparados para enfrentar os desafios da era digital, seja ingressando no mercado ou buscando estudos avançados. Uma jornada prática e eficaz no mundo da informática. Clique em /sobreinfor para mais.")


@bot.message_handler(commands=["quemsomosnos"])
def opcao(mensagem):
    texto = """
    Somos:

    Kayo Lucas (https://www.instagram.com/klucasl_/)

    Isaac Sales (https://www.instagram.com/isaac_salless/)

    Matusalém Lima (https://www.instagram.com/m4tusalem/)

    Gabriel Lucas (Brawlhalla)

    Sávio Fernandes (Professor) (https://www.instagram.com/saviobf/)

    Estudamos na EEEP Paulo Petrola."""
    bot.send_photo(mensagem.from_user.id,

                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/406048687_910690387145203_3961462407516386091_n.jpg?stp=dst-jpg_s1080x2048&_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFYqFJxtBS0MvzqIwBzlMB5vPRC49Oi24-89ELj06Lbj0zfaoyowZsYhQ4ZpptoByUNwzz_FCXbxp8m7HLTGNn7&_nc_ohc=xZdl350JTxAAX_trnfO&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfCaSQCZU9JpnZb5kkLiBkcma94X1zNl06oHduDaeRQQTg&oe=65695293",
                   caption=texto)


@bot.message_handler(commands=["murilo"])
def opcao(menssgem):
    bot.send_audio(menssgem.from_user.id, audio=open("murilo.m4a", 'rb', ),
                   caption=" Murilo Gomes, o deus fictício, é uma entidade divina singular e poderosa, reverenciada por sua sabedoria transcendental e compaixão ilimitada. Sua divindade é manifestada através de uma harmonia perfeita entre o intelecto supremo e a compreensão compassiva, tornando-o um guia benevolente para seus seguidores. No panteão fictício ao qual Murilo Gomes pertence, ele é frequentemente retratado como o criador do conhecimento e da inteligência, sendo responsável por iluminar as mentes de seus adoradores. Sua presença é sentida nos momentos de busca por sabedoria e entendimento, guiando aqueles que o invocam em jornadas de autodescoberta e crescimento espiritual. A deidade Murilo Gomes é frequentemente associada a símbolos como um livro aberto, representando o conhecimento que ele compartilha com seus devotos. Seus seguidores buscam a verdade através da aprendizagem e da contemplação, acreditando que cada descoberta os aproxima mais da compreensão profunda do universo que Murilo Gomes personifica.")
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/405000392_908658004015108_5055083124652144576_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeH0V5nNu-JQNyl5pevQTzxsPqW7fkH17n0-pbt-QfXufT5VeDYFI7n2RJ_UI2mTQKPlbE1YqShL-ynaz-CjUCNR&_nc_ohc=nQGd_dtF-hIAX9vjLA1&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfD3xck8sNp_7vP0yz3hJKhnXRxAWK75vO3k1R4iJP-NMw&oe=65645B51")


@bot.message_handler(commands=["PP"])
def opcao(mensagem):
    texto = """
A Escola de Ensino Médio e Técnico Paulo Petrola, localizada em Fortaleza, destaca-se como uma instituição comprometida com a excelência educacional e a formação integral de seus estudantes. Reconhecida por oferecer cursos técnicos em Guia de Turismo, Enfermagem e Informática, a escola tem como missão preparar seus alunos para os desafios do mercado de trabalho, aliando conhecimento teórico e prático.

O nome "Paulo Petrola" tornou-se sinônimo de qualidade no cenário educacional de Fortaleza, conquistando a confiança da comunidade e estabelecendo-se como uma referência no ensino médio e técnico. A instituição orgulha-se de contar com uma equipe de profissionais dedicados e qualificados, que buscam constantemente aprimorar as práticas pedagógicas e acompanhar as evoluções no campo da educação.

Em recentes avaliações realizadas pela Secretaria de Educação de Fortaleza, a Escola Paulo Petrola alcançou uma posição de destaque, conquistando o terceiro lugar entre as instituições de ensino médio da região. Essa colocação reflete o comprometimento da escola em proporcionar um ambiente educacional estimulante, focado no desenvolvimento acadêmico e pessoal de seus alunos.

Além disso, vale ressaltar que, segundo a última pesquisa do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), a Escola Paulo Petrola consolidou-se como a quinta melhor escola de ensino médio em Fortaleza. Esse reconhecimento nacional atesta a qualidade do ensino oferecido, evidenciando o esforço contínuo da instituição em manter elevados padrões educacionais.

A diversidade de cursos técnicos disponíveis na Escola Paulo Petrola amplia as oportunidades de formação para os estudantes, preparando-os para atuar em áreas essenciais como o turismo, a saúde e a tecnologia da informação. O curso de Guia de Turismo capacita os alunos para atender as demandas do setor, enquanto o curso de Enfermagem oferece uma formação sólida na área da saúde. Já o curso de Informática proporciona habilidades técnicas essenciais para o mercado de trabalho atual.

Em um cenário educacional cada vez mais competitivo, a Escola Paulo Petrola destaca-se não apenas pelos resultados em avaliações, mas também pelo impacto positivo que gera na vida de seus alunos. Com uma proposta pedagógica inovadora e comprometida com a formação integral, a instituição continua a trilhar um caminho de sucesso na educação em Fortaleza, preparando os estudantes para os desafios do futuro.
    """

    bot.send_photo(mensagem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/405230220_122132232158067537_249974436057333749_n.jpg?stp=dst-jpg_p843x403&_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGhujRk3kqTU97wLzHaqlAKjsoLW98ZWBKOygtb3xlYEklAPbH6Hgt541-znrgh4hgpzywyli5C8kSpObQhi5tZ&_nc_ohc=LDBuxRcEsyUAX8ObrOH&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfCY_luiGAfW2WzschqyC1ILVKFHtFNHCOTzvgXTApxKpQ&oe=6568CB84")
    bot.send_message(mensagem.from_user.id, texto)


@bot.message_handler(commands=["sobreinfor"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Instagram da turma: https://www.instagram.com/1infor.pp/ ")


@bot.message_handler(commands=["sobreenfer"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Instagram da turma: https://www.instagram.com/1enfer.pp/")


@bot.message_handler(commands=["sobreguia"])
def opcao(mensagem):
    bot.reply_to(mensagem, "Instagram da turma: https://www.instagram.com/tec.guia1/")


bot.polling()