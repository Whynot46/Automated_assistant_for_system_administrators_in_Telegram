Проект с открытым исходным кодом "Автоматизированный помощник для системных администраторов в Telegram"

1) Запустите файл install_python.bat для установки интерпретатора Python.
(Если у вас уже установлен интерпретатор Python версии 3.7 и выше, пропустите этот шаг)

2) Запустите файл install_libraries.bat для установки необходимых библиотек и обновления пакетного менеджера pip.

3) В Telegram запустите бота @BotFather командой /start . Для создания бота введите в чате с BotFather команду /newbot.
Бот попросит вас ввести название для нового бота. Можете указать в любом удобном формате, поддерживается кириллица и латиница, например: «тестовый bot». — Имя будет отображаться в заголовке и в информации о боте.
После того, как вы дали боту имя, нужно указать его сокращенное название для ссылок. Оно должно обязательно содержат приставку «bot» на конце. Например: «Test_bot». — Сокращенное название может содержать от 5 до 32 и только латинских символов.
Если все выполнено верно ваш бот будет зарегистрирован в Телеграм и BotFather выдаст вам токен бота в таком формате: "764645301:AAGdRMMi_bF67lCkJjA0DKQNOwoATJQMWXk" .
Здесь же, в @BotFather введите команду /mybots. Далее выберите созданного бота. Перейдите в Bot Settings → Group Privacy. Выберите "Turn off". Должна появиться фраза "Privacy mode is disabled for Bot".

4) Вставьте полученный API_KEY в файл src/IDs.py в строке " API_KEY = ". Важно! Вставляемый вами ключ должен быть заключён в кавычки!

5) Создайте новый канал в Telegram, добавьте созданного вами бота и повысьте его до администратора. В этот канал будут отправляться уже сформированные заявки.

6) Вам необходимо указать ID канала, в который будет производиться отправка сформированных заявок, а также указать ID пользователей, которые будут иметь доступ к панели администратора.
Запустите бота @chatIDrobot и отправьте ему сообщение с любым текстом. В ответ бот отправит вам подробную информацию об отправителе, включая нужный вам ID пользователя в формате: " 1091349364 ".
Чтобы узнать ID канала, отправьте в канал любое сообщение от администратора и перешлите его в бота @chatIDrobot, после чего бот отправит вам подробную информацию о канале, 
также включая нужный вам ID канала в формате: " -1091815564673 ".

Вставьте ID канала в файл src/IDs.py в строке " main_chanel_id = ". Важно! Вставляемый вами ID должен быть заключён в кавычки!
Вставьте ID администратор в файл src/IDs.py в строке " admin_id = " внутри квадратных скобок через запятую. Важно! Каждый вставляемый вами ID должен быть заключён в кавычки!

9) Готово! Теперь ваше устройство готово к запуску бота! Запустите файл start.bat и пейте чаёк с печеньками, пока ваш бот собирает для вас заявки!


*Опционально: Если вы хотите положить вашего бота в автозагрузку, то: 
1) Создайте ярлык файла start.bat .
2) Нажмите комбинацию Win+R или в панели Пуск введите "Выполнить".
3) В появившимся окне введите "shell:startup"
4) В открывшуюся папку поместите созданный вам ярлык.

Поздравляю вас, вы прекрасны!

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

Open source project "Automated assistant for system administrators in Telegram"

1) Run the install_python.bat file to install the Python interpreter.
(If you already have Python interpreter version 3.7 or later installed, skip this step)

2) Run the install_libraries.bat file to install the necessary libraries and update the pip package manager.

3) In Telegram, start the @BotFather bot with the /start command. To create a bot, enter the /newbot command in a chat with BotFather.
The bot will ask you to enter a name for the new bot. You can specify in any convenient format, Cyrillic and Latin are supported, for example: "test bot". - The name will be displayed in the title and in the information about the bot.
After you have given the bot a name, you need to specify its short name for links. It must necessarily contain the prefix "bot" at the end. For example: "Test_bot". — The abbreviated name can contain from 5 to 32 and only Latin characters.
If everything is done correctly, your bot will be registered in Telegram and BotFather will give you a bot token in the following format: "764645301:AAGdRMMi_bF67lCkJjA0DKQNOwoATJQMWXk" .
Here, in @BotFather, enter the /mybots command. Next, select the created bot. Go to Bot Settings → Group Privacy. Select "Turn off". The phrase "Privacy mode is disabled for Bot" should appear.

4) Paste the resulting API_KEY into the IDs.py file at the " API_KEY = " line. Important! The key you insert must be enclosed in quotes!

5) Create a new channel in Telegram, add the bot you created and promote it to admin. Already formed applications will be sent to this channel.

6) You need to specify the ID of the channel to which generated requests will be sent, as well as specify the IDs of users who will have access to the admin panel.
Launch the @chatIDrobot bot and send him a message with any text. In response, the bot will send you detailed information about the sender, including the user ID you need in the format: " 1091349364 ".
To find out the channel ID, send any message from the administrator to the channel and forward it to the @chatIDrobot bot, after which the bot will send you detailed information about the channel,
also including the channel ID you want in the format: "-1091815564673".

Paste the channel ID into the IDs.py file at the " main_chanel_id = " line. Important! The ID you insert must be enclosed in quotes!
Paste the admin ID into the IDs.py file on the line " admin_id = " inside square brackets separated by commas. Important! Each ID you insert must be enclosed in quotes!

9) Done! Your device is now ready to run the bot! Run the file start.bat and drink tea and cookies while your bot collects applications for you!


*Optional: If you want to autoload your bot, then:
1) Create a shortcut to the start.bat file.
2) Press the combination Win + R or in the Start panel, type "Run".
3) In the window that appears, enter "shell:startup"
4) In the folder that opens, place the shortcut you created.

Congratulations, you are wonderful!

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

Thanks for downloading!
My GitHub: https://github.com/Whynot46
