from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- 1. CONFIGURAÇÕES ---
# ⚠️ SUBSTITUA PELO SEU TOKEN REAL
TOKEN = "8417108186:AAGoqgdRxqEz81fJn6f5wJGg0m2tNefAoIc"
# ⚠️ SUBSTITUA PELO LINK DO SEU CANAL REAL
CANAL_LINK = "https://t.me/+PG7sb9vyd25mZWRh"
BOTAO_TEXTO = "👉 Entrar no Canal Exclusivo"

# --- 2. FUNÇÃO MANIPULADORA DO COMANDO /START ---

# A função 'start' é assíncrona (async) e é chamada quando o usuário envia /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem de boas-vindas com um botão para o canal."""
    
    # 2.1. Cria o Botão Inline (URL Button)
    # O argumento 'url' é o que faz o botão abrir o link
    keyboard = [
        [InlineKeyboardButton(BOTAO_TEXTO, url=CANAL_LINK)]
    ]
    
    # 2.2. Cria o Markup (o teclado/conjunto de botões)
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # 2.3. Mensagem que será enviada ao usuário
    mensagem_saudacao = (
        f"Olá, {update.effective_user.first_name}!\n\n"
        "Seja bem-vindo(a) ao nosso bot.\n\n"
        "Para acessar todo o nosso conteúdo e não perder nenhuma novidade, "
        "é necessário que você entre no nosso **Canal Exclusivo** no Telegram.\n\n"
        "Clique no botão abaixo para participar:"
    )
    
    # 2.4. Envia a mensagem com os botões
    # 'reply_text' é usado para responder ao usuário
    # 'parse_mode="MarkdownV2"' permite o uso de negrito (**)
    await update.message.reply_text(
        mensagem_saudacao,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# --- 3. EXECUÇÃO PRINCIPAL ---

def main() -> None:
    """Inicia o bot."""
    
    # 3.1. Cria a Aplicação e passa o Token
    application = Application.builder().token(TOKEN).build()
    
    # 3.2. Registra o manipulador de comando para /start
    # Sempre que o usuário digitar /start, a função 'start' será chamada
    application.add_handler(CommandHandler("start", start))
    
    # 3.3. Inicia o Polling (o bot começa a "escutar" por novas mensagens)
    print("Bot rodando... Pressione Ctrl+C para parar.")
    application.run_polling(poll_interval=3) # Verifica novas mensagens a cada 3 segundos

if __name__ == '__main__':
    main()