import telebot
import openai

bot = telebot.TeleBot("************************************************") //BotFather API key
openai.api_key = "sk-************************************************"  //OpenAI key


@bot.message_handler(content_types=['text'])
def lalala(message):
    print(message.chat.title, message.chat.username)
    if message.chat.id == ******** : // groupID
        # print(message.text)
        if "************" in message.text: // _nameBot
            message.text = (message.text).replace("*********", "") // _nameBot
            # print(message.text)
            response = openai.Completion.create(model="text-davinci-003", prompt=message.text, max_tokens=1000)
            full_response = response['choices'][0][
                'text']  # Use the text property of the first element of the choices list to access the full response
            lines = full_response.splitlines()  # Split the response into individual lines
            for line in lines:  # Iterate over the lines
                try:
                    # print(line)
                    bot.send_message(message.chat.id, line)  # Send each line back to the user as a separate message
                except Exception as e:
                    print(e)
    else:
        bot.send_message(message.chat.id, "***************") // TexT


bot.polling(none_stop=True, interval=0)