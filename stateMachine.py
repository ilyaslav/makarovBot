from transitions import Machine

class StateMachine(object):
    pass

states=['main_menu',
        'training',
        'gym_training',
        'change_gym_training',
        'load_gym_training',
        'home_training',
        'change_home_training',
        'training_profile',
        'change_profile',
        'male',
        'female',
        'gain_muscle_mass',
        'weight_loss',
        'maintaining_muscle_mass',
        'workouts_2',
        'workouts_3',
        'add_training_record',
        'get_training_record',
        'necessary_equipment',
        'change_necessary_equipment',
        'base_of_exercises',
        'legs',
        'breast',
        'back',
        'shoulders',
        'biceps',
        'triceps',
        'press',
        'stretching',
        'MFR',
        'add_exercise_video',
        'exercises_video',
        'tariffs',
        'tarif1',
        'tarif2',
        'manual',
        ]

transitions = [
    { 'trigger': 'back', 'source': 'tariffs', 'dest': 'main_menu' },
    { 'trigger': 'back', 'source': 'necessary_equipment', 'dest': 'main_menu' },
    { 'trigger': 'back', 'source': 'training', 'dest': 'main_menu' },
    { 'trigger': 'back', 'source': 'base_of_exercises', 'dest': 'main_menu' },
    { 'trigger': 'back', 'source': 'manual', 'dest': 'main_menu' },
    { 'trigger': 'back', 'source': 'tarif1', 'dest': 'tariffs' },
    { 'trigger': 'back', 'source': 'tarif2', 'dest': 'tariffs' },
    { 'trigger': 'back', 'source': 'legs', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'breast', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'back', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'shoulders', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'biceps', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'triceps', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'press', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'stretching', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'MFR', 'dest': 'base_of_exercises' },
    { 'trigger': 'back', 'source': 'exercises_video', 'dest': 'exercise' },
    { 'trigger': 'back', 'source': 'add_exercise_video', 'dest': 'exercise' },
    { 'trigger': 'back', 'source': 'gym_training', 'dest': 'training' },
    { 'trigger': 'back', 'source': 'home_training', 'dest': 'training' },
    { 'trigger': 'back', 'source': 'training_profile', 'dest': 'training' },
    { 'trigger': 'back', 'source': 'change_gym_training', 'dest': 'gym_training' },
    { 'trigger': 'back', 'source': 'load_gym_training', 'dest': 'change_gym_training' },
    { 'trigger': 'back', 'source': 'change_home_training', 'dest': 'home_training' },
    { 'trigger': 'back', 'source': 'change_profile', 'dest': 'training_profile' },
    { 'trigger': 'back', 'source': 'add_training_record', 'dest': 'training_profile' },
    { 'trigger': 'back', 'source': 'get_training_record', 'dest': 'training_profile' },
    { 'trigger': 'back', 'source': '', 'dest': '' },
    { 'trigger': 'back', 'source': '', 'dest': '' },
    { 'trigger': 'back', 'source': '', 'dest': '' },
    { 'trigger': 'back', 'source': '', 'dest': '' },
    { 'trigger': 'back', 'source': '', 'dest': '' },
    { 'trigger': 'back', 'source': '', 'dest': '' },
    { 'trigger': 'back', 'source': '', 'dest': '' },
]

def back_state(state: str) -> str:
    st = StateMachine()
    machine = Machine(st, states=states, transitions=transitions, initial=state)
    try:
        st.trigger('back')
    finally:
        return st.state
