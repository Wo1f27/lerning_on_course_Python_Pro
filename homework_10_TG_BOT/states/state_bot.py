from aiogram.fsm.state import State, StatesGroup


class MenuState(StatesGroup):
    main_start_state = State()
    add_note = State()
    delete_note = State()
