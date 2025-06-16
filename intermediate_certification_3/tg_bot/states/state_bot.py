from aiogram.fsm.state import State, StatesGroup


class MenuState(StatesGroup):
    main_start_state = State()
    add_task = State()
    add_task_deadline = State()
    delete_task = State()
