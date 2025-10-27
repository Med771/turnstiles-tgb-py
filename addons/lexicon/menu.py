class MenuLexicon:
    ADMIN_PANEL_TEXT = (
        "⚙️ *Панель администратора турникетов*\n\n"
        "_Выберите действие:_"
    )

    USER_PANEL_TEXT = (
        "⚠️ *Доступ запрещён*\n\n"
        "У вас нет прав для входа в административную панель.\n"
        "Пожалуйста, обратитесь к *администратору*."
    )

    BACK: str = "🔙 Вернуться назад"
    BACK_CALL: str = "back"
    SPEC_BACK_CALL: str = "spec_back_"

    ADD: str = "🆕 Добавить пользователя"
    ADD_CAL: str = "add_new_user"

    FIND: str = "🔄 Найти пользователя"
    FIND_CALL: str = "find_user"
