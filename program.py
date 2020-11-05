from datetime import datetime
import time
import random



_color_list = ('red','green','blue','indigo','firebrick','fuchsia','lawngreen',
              'chocolate','orange','brown','purple','olive','coral','lavender',
              'maroon','gold','crimson','magenta','cyan','tomato','bisque')

_clock_face_color = 'lavender'
_hour_label_color = 'black'
_wall_color = 'lavender'

_default_date_str = "03/11/2020"
_default_time_str = "12:00:00"
_default_datetime = datetime.strptime(f'{_default_date_str} {_default_time_str}', '%d/%m/%Y %H:%M:%S')

_total_servers_running = 0
_total_servers_stopped = 0


def check_event(program_time, wall_color, clock_face_color, hour_label_color): 
    tasks = []
    messages = []
   
    actual_time = datetime.strftime(datetime.now(), "%I:%M:%S%p").lower()
    program_datetime = datetime.strptime(f'{_default_date_str} {program_time}', '%d/%m/%Y %H:%M:%S')
    time_difference = program_datetime - _default_datetime
    seconds_elapsed = time_difference.seconds
    
    if seconds_elapsed % 30 == 0:
        tasks.append('START')
        started_servers = start_servers([wall_color, clock_face_color])
        messages.append(f'Start {started_servers} servers')
        
        
    if seconds_elapsed % 40 == 0:
        tasks.append('STOP')
        stopped_servers = stop_servers([wall_color, clock_face_color])
        messages.append(f'Stop {stopped_servers} servers')
        
    if seconds_elapsed % 50 == 0:
        tasks.append('STOP')
        report_servers([hour_label_color,])
        messages.append(f'Report {_total_servers_running} servers running')

    ui_message = f'{program_time} - {", ".join(messages)}'.lower()
    data = {'message': ui_message, 'wall_color': _wall_color,
            'clock_color': _clock_face_color, 'label_color': _hour_label_color}
    return data
    
    
    

def start_servers(excluded_colors):
    global _wall_color, _total_servers_running
    _wall_color = get_random_color(excluded_colors)
    started_servers = random.randint(10, 20)
    _total_servers_running += started_servers
    return started_servers
    

def stop_servers(excluded_colors):
    global _clock_face_color, _total_servers_running
    _clock_face_color = get_random_color(excluded_colors)
    stopped_servers = (random.randint(5, _total_servers_running) 
                       if _total_servers_running >= 5 else _total_servers_running)    
    _total_servers_running -= stopped_servers
    return stopped_servers
    

def report_servers(excluded_colors):
    global _hour_label_color
    _hour_label_color = get_random_color(excluded_colors)
    
    

def get_full_report():
    pass

def get_random_color(excluded=[]):
    color_choices = list(x for x in _color_list if x not in excluded)
    random_color = random.choice(color_choices)
    return random_color

def reset_values():
    _total_servers_running = 0
    _total_servers_stopped = 0

    