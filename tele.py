import telebot
import threading
import schedule
from time import time, sleep
from tabulate import tabulate
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineQueryResultArticle
from telebot.types import InputTextMessageContent

chave = "6028892799:AAFiKNAdqTzqcRHXcqdoPlykDx1k255fTaU"
chat_id = "1427119084"

bot = telebot.TeleBot(chave)


@bot.message_handler(commands=["start"])
def responder(inicio):
    texto = """
    Somos:
    Kayo Lucas (https://www.instagram.com/klucasl_/)
    Isaac Sales (https://www.instagram.com/isaac_salless/)
    Matusalém Lima (https://www.instagram.com/m4tusalem/)
    Gabriel Lucas
    Estudamos na EEEP Paulo Petrola."""
    
    bot.send_photo(inicio.from_user.id,
                   photo="https://scontent-for1-1.xx.fbcdn.net/v/t39.30808-6/402106565_907740337440208_6687529766115017951_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeGHgnQIupxFBNmxHjvx3JmA7AZIGqr8SJXsBkgaqvxIlSntaP6C6YAjdV-68Va-rjfMho7fac1teUK1Sj8_rGaW&_nc_ohc=BK-qeocueMEAX9oEc0O&_nc_ht=scontent-for1-1.xx&oh=00_AfBSGj__F4h0I8P7BV9jBrJbKwrgp5yAq4smbQegkfHCTg&oe=65621DB7",
                   caption="Ola! Somos a loja Murilo Gomes, temos como objetivo vender cursos!. Digite /cursos para os nossos cursos ou /empresa para conhecer nossa empresa.")
    bot.send_message(inicio.from_user.id, texto)


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
        bot.send_audio(menssgem.from_user.id, audio=open("murilo.m4a", 'rb',), caption=" Murilo Gomes, o deus fictício, é uma entidade divina singular e poderosa, reverenciada por sua sabedoria transcendental e compaixão ilimitada. Sua divindade é manifestada através de uma harmonia perfeita entre o intelecto supremo e a compreensão compassiva, tornando-o um guia benevolente para seus seguidores. No panteão fictício ao qual Murilo Gomes pertence, ele é frequentemente retratado como o criador do conhecimento e da inteligência, sendo responsável por iluminar as mentes de seus adoradores. Sua presença é sentida nos momentos de busca por sabedoria e entendimento, guiando aqueles que o invocam em jornadas de autodescoberta e crescimento espiritual. A deidade Murilo Gomes é frequentemente associada a símbolos como um livro aberto, representando o conhecimento que ele compartilha com seus devotos. Seus seguidores buscam a verdade através da aprendizagem e da contemplação, acreditando que cada descoberta os aproxima mais da compreensão profunda do universo que Murilo Gomes personifica.")
        bot.send_photo(menssgem.from_user.id, photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/405000392_908658004015108_5055083124652144576_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeH0V5nNu-JQNyl5pevQTzxsPqW7fkH17n0-pbt-QfXufT5VeDYFI7n2RJ_UI2mTQKPlbE1YqShL-ynaz-CjUCNR&_nc_ohc=nQGd_dtF-hIAX9vjLA1&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfD3xck8sNp_7vP0yz3hJKhnXRxAWK75vO3k1R4iJP-NMw&oe=65645B51")

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


@bot.message_handler(commands=["Gari"])
def opcao(menssgem):
    bot.send_photo(menssgem.from_user.id,
                   photo="https://scontent.ffor7-1.fna.fbcdn.net/v/t39.30808-6/404373869_122130462380067537_1224380065145938493_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHoqKEvZzksM9P_cAPnj70zDL2HsVOAJkIMvYexU4AmQo_XmmI3-74_hYsVGdym-vM-qwurXhXmbqdwc0_TsEPT&_nc_ohc=Jku65upCH7oAX8pYDXA&_nc_zt=23&_nc_ht=scontent.ffor7-1.fna&oh=00_AfBHrc69q9Q7SZQJnCqRH7pKiC1CJ590jsjiUNhCmIfC2A&oe=65613D1C",
                   caption="Este curso aborda a importância da coleta de resíduos, destacando práticas sustentáveis e métodos eficientes de gestão de resíduos. Os participantes aprenderão sobre a segurança e as melhores práticas associadas à profissão de gari, contribuindo para um ambiente mais limpo e saudável. Assine o nosso curso: /CompraGari")



bot.polling()


config = {

    "apiKey"              : "",
    "authDomain"          : "",
    "databaseURL"         : "",
    "projectId"           : "",
    "storageBucket"       : "",
    "messagingSenderId"   : "",
    "appId"               : "",
    "measurementId"       : "",  
}                                   # Your FIREBASE DATABASE configurations

def emoji_board(game):              # Creates the board in ASCII format
    emojis = {"-":"-", "x":"x","o":"o"}
    board, temp = [], []
    for count, _ in enumerate(game, 1):
        if count == len(game):
            temp.append(emojis[_])
            board.append(temp)
        elif count % 3 != 0:
            temp.append(emojis[_])
        else:
            temp.append(emojis[_])
            board.append(temp)
            temp = []

    return tabulate(board, tablefmt="grid")

def check_win(game, game_id):       # Checks the status of the game  

    wins = [
        (0,1,2), (3,4,5), (6,7,8), (0,4,8),
        (0,3,6), (1,4,7), (2,5,8), (2,4,6),
    ]
    
    for win in wins:

        C1 = (game[win[0]], game[win[1]], game[win[2]]) == ("x","x","x")
        C2 = (game[win[0]], game[win[1]], game[win[2]]) == ("o","o","o")

        if C1 or C2:
            bot.edit_message_reply_markup(inline_message_id=game_id, reply_markup=None)
            winner = "X" if C1 else "O"
            bot.edit_message_text(inline_message_id=game_id, text=f"<b>Congratulations! 🎉\n\
            \nPlayer {winner} wins! 🥳\n\n<code>{emoji_board(game)}</code></b>")
            database.child(game_id).remove()
            return "True"
    else:
        if "-" not in game: return "Draw"
        else:   return "False"

firebase = pyrebase.initialize_app(config)
database = firebase.database()

API_KEY = "6028892799:AAFiKNAdqTzqcRHXcqdoPlykDx1k255fTaU"    # API TOKEN from @BotFather
BANNER  = ""    # FILE ID of banner for your bot

bot = telebot.TeleBot(API_KEY, parse_mode="HTML")   # Initializing the bot

def remove_expired():   # Deletes all expired games
    try:
        for game in database.get().each():
            expiry, id = int(game.val()["expiry"]), game.val()["id"]
            if int(time()) - expiry >= 300:
                database.child(id).remove()
                bot.edit_message_text(inline_message_id=id, text="<b>Game expired! 🙃</b>")
                bot.edit_message_reply_markup(inline_message_id=id, reply_markup=None)
    except:
        pass

def create_game_board(game):    # Creates a new empty game board

    game_board, buttons = InlineKeyboardMarkup(row_width = 3), []

    for pos, _ in enumerate(game, 1):
        buttons.append(InlineKeyboardButton(_, callback_data=f'{pos}'))
    game_board.add(*buttons)

    return game_board

@bot.message_handler(commands="start")
def start(message):                     # Starts the bot

    bot.send_photo(message.chat.id, BANNER, caption="<b>Wanna a play a game of Tic-Tac-Toe?\n\
    \nClick the buton and play with your friends!</b>",
    reply_markup = InlineKeyboardMarkup().row(InlineKeyboardButton("Play Tic-Tac-Toe!",
    switch_inline_query="tic_tac_toe")))

@bot.inline_handler(lambda query: len(query.query) == 0 or query.query == 'tic_tac_toe')   
def send_game(query):       # Creating the inline query handler

    play = InlineKeyboardMarkup().row(InlineKeyboardButton("Tap to play!",
    callback_data=f"play{query.from_user.id}"))

    try:
        t_t_t = InlineQueryResultArticle('start_game',"丅Ꭵᑕ-丅ᗩᑕ-丅ᗝᗴ",
        InputTextMessageContent("<b>Start the game! 🥳\n\nGame will be expire in 5 minutes!</b>",
        parse_mode = "HTML"),reply_markup = play,
        description = "Play a game of Tic-Tac-Toe with your friends and family! ✌🏻",
        thumb_url = "https://github.com/TECH-SAVVY-GUY/telegram-games/blob/master/assets/tic-tac-toe.jpg?raw=true")
        bot.answer_inline_query(query.id, [t_t_t])
    except:
        pass

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):                        # A single callback listener for all calls

    data, game_id = call.data, call.inline_message_id
   
    if data[:4] == "play":              # Starting the game
        
        player_x, player_o = int(data[4:]), int(call.from_user.id)

        if player_o == player_x:
            bot.answer_callback_query(call.id,
            "⚠️ Must be a different player! ⚠️", show_alert=True)
        else:
            bot.edit_message_text(inline_message_id=game_id, text="<b>Game in progress!</b>")
            bot.edit_message_reply_markup(inline_message_id=game_id,
            reply_markup=create_game_board(["-"] * 9))

            database.child(game_id).child("id").set(game_id)
            database.child(game_id).child("player_x").set(int(data[4:]))
            database.child(game_id).child("player_o").set(call.from_user.id)
            database.child(game_id).child("count").set(1)
            database.child(game_id).child("board").set(f"{['-'] * 9}")
            database.child(game_id).child("expiry").set(int(time()))

    elif data.isnumeric():      # Player move algorithm

        if int(data) in range(1,10):

            game = database.child(game_id).get()
            players = [int(game.val()["player_x"]), int(game.val()["player_o"])]
            
            if call.from_user.id not in players:
                bot.answer_callback_query(call.id,
                "❌  You are not a player!  ❌", show_alert=True)
            else: 
                count = int(game.val()["count"])
                
                if count % 2 != 0:
                    if call.from_user.id != players[0]:
                        bot.answer_callback_query(call.id,
                            "⚠️ Wait for your Turn! ⚠️", show_alert=True)
                    else:
                        board = eval(game.val()["board"])
                        if board[int(data)-1] == "-":
                            board[int(data)-1] = "x"
                            bot.edit_message_reply_markup(inline_message_id=game_id,
                            reply_markup=create_game_board(board))    
                            stat = check_win(board, game_id)
                            if stat != "True":
                                if str(stat) == "Draw":
                                    bot.edit_message_reply_markup(inline_message_id=game_id, reply_markup=None)
                                    bot.edit_message_text(inline_message_id=game_id,
                                    text = f"<b>It's a draw! 🥱\n\n<code>{emoji_board(board)}</code></b>")
                                    database.child(game_id).remove()                             
                                else:
                                    database.child(game_id).update({"board":str(board)})
                                    database.child(game_id).update({"count":count + 1})  

                else:
                    if call.from_user.id != players[-1]:
                        bot.answer_callback_query(call.id,
                            "⚠️ Wait for your Turn! ⚠️", show_alert=True)
                    else:
                        board = eval(game.val()["board"])
                        if board[int(data)-1] == "-": 
                            board[int(data)-1] = "o"
                            bot.edit_message_reply_markup(inline_message_id=game_id,
                            reply_markup=create_game_board(board))    
                            stat = check_win(board, game_id)
                            if stat != "True":
                                if str(stat) == "Draw":
                                    bot.edit_message_reply_markup(inline_message_id=game_id, reply_markup=None)
                                    bot.edit_message_text(inline_message_id=game_id,
                                    text = f"<b>It's a draw! 🥱\n\n<code>{emoji_board(board)}</code></b>")  
                                    database.child(game_id).remove()                                                               
                                else:
                                    database.child(game_id).update({"board":str(board)})
                                    database.child(game_id).update({"count":count + 1})                                   

def thrd():         # Scheduling the deletion of expired games
    while True:
        schedule.run_pending()
        sleep(1)

schedule.every(1).minutes.do(remove_expired)
t = threading.Thread(target=thrd)               # Creating a seperate thread

def main():     # Executing all the threads
    t.start()      
    bot.infinity_polling()