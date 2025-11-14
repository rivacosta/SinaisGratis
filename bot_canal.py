import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- 1. CONFIGURAÇÕES DE SEGURANÇA E AMBIENTE ---
# Carrega as variáveis do arquivo .env (deve estar na mesma pasta)
load_dotenv()

# Tenta ler o TOKEN do ambiente (do arquivo .env ou do sistema)
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    # Se o token não for encontrado, o bot não deve iniciar
    raise ValueError("TELEGRAM_TOKEN não encontrado. Crie um arquivo .env com a variável.")

# --- 2. OUTRAS CONFIGURAÇÕES ---
# ⚠️ SUBSTITUA PELO LINK DO SEU CANAL REAL (este valor pode ficar aqui)
CANAL_LINK = "https://t.me/+PG7sb9vyd25mZWRh"
BOTAO_TEXTO = "👉 Entrar no Canal Exclusivo"


# --- 3. FUNÇÃO MANIPULADORA DO COMANDO /START ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem de boas-vindas com um botão para o canal."""
    
    # 3.1. Cria o Botão Inline (URL Button)
    keyboard = [
        [InlineKeyboardButton(BOTAO_TEXTO, url=CANAL_LINK)]
    ]
    
    # 3.2. Cria o Markup (o teclado/conjunto de botões)
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # 3.3. Mensagem que será enviada ao usuário
    mensagem_saudacao = (
        f"Olá, {update.effective_user.first_name}!\n\n"
        "Seja bem-vindo(a) ao nosso bot.\n\n"
        "Para acessar todo o nosso conteúdo e não perder nenhuma novidade, "
        "é necessário que você entre no nosso **Canal Exclusivo** no Telegram.\n\n"
        "Clique no botão abaixo para participar:"
    )
    
    # 3.4. Envia a mensagem com os botões
    await update.message.reply_text(
        mensagem_saudacao,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# --- 4. EXECUÇÃO PRINCIPAL ---

def main() -> None:
    """Inicia o bot."""
    
    # 4.1. Cria a Aplicação e passa o Token lido do .env
    application = Application.builder().token(TOKEN).build()
    
    # 4.2. Registra o manipulador de comando para /start
    application.add_handler(CommandHandler("start", start))
    
    # 4.3. Inicia o Polling
    print("Bot rodando... Pressione Ctrl+C para parar.")
    application.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()

