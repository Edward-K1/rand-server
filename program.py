import time
import random
import uuid

from datetime import datetime
from db import servers_db



_color_list = ('red','green','blue','indigo','firebrick','fuchsia','lawngreen',
              'chocolate','orange','brown','purple','olive','coral','lavender',
              'maroon','gold','crimson','magenta','cyan','tomato','bisque')

_default_date_str = "03/11/2020"
_default_time_str = "12:00:00"
_default_datetime = datetime.strptime(f'{_default_date_str} {_default_time_str}', '%d/%m/%Y %H:%M:%S')


def run_task(server_id, program_time, wall_color, clock_face_color, hour_label_color): 
    random_server = ''
    for server in servers_db:
        if server.get_id() == server_id:
            random_server = server

   
    actual_time = datetime.strftime(datetime.now(), "%I:%M:%S%p").lower()
    program_datetime = datetime.strptime(f'{_default_date_str} {program_time}', '%d/%m/%Y %H:%M:%S')
    time_difference = program_datetime - _default_datetime
    seconds_elapsed = time_difference.seconds
    
    if seconds_elapsed % 30 == 0:
        random_server.start_servers(program_time, actual_time, [wall_color, clock_face_color])
        
    if seconds_elapsed % 40 == 0:
        random_server.stop_servers(program_time, actual_time,[wall_color, clock_face_color])
  
    if seconds_elapsed % 50 == 0:
        random_server.report_servers(program_time, actual_time,[hour_label_color])

    response = random_server.get_response_data(program_time)
    return response


def get_full_report():
    random_server = ''
    for server in servers_db:
        if server.get_id() == server_id:
            random_server = server
    return random_server.get_report()


def create_server():
    random_server = RandomServer()
    servers_db.append(random_server)
    response_data = {'server_id':random_server.get_id()}
    return response_data


def get_random_color(excluded=[]):
    color_choices = list(x for x in _color_list if x not in excluded)
    random_color = random.choice(color_choices)
    return random_color


class RandomServer:
    def __init__(self):
        self.__id = uuid.uuid4().hex
        self.start_time = datetime.now()
        self.running_servers = 0
        self.stopped_servers = 0
        self.clock_color = 'lavender'
        self.wall_color = 'chocolate'
        self.label_color = 'black'
        self.program_time = ''
        self.actual_time = ''
        self.tasks = []
        self.messages = []
        self.event_log = []

    def get_id(self):
        return self.__id

    def start_servers(self, program_time, actual_time, excluded_colors):
        self.program_time, self.actual_time = program_time, actual_time
        self.tasks.append('START')
        self.wall_color = get_random_color(excluded_colors)
        started_servers = random.randint(10, 20)
        self.running_servers += started_servers
        self.messages.append(f'Start {started_servers} servers')
        return started_servers

    def stop_servers(self, program_time, actual_time, excluded_colors):
        self.program_time, self.actual_time = program_time, actual_time
        self.tasks.append('STOP')
        self.clock_color = get_random_color(excluded_colors)
        stopped_servers = (random.randint(5, self.running_servers) 
                       if self.running_servers >= 5 else self.running_servers)
        self.running_servers -= stopped_servers
        self.stopped_servers += stopped_servers
        self.messages.append(f'Stop {stopped_servers} servers')
        return stopped_servers

    def report_servers(self, program_time, actual_time, excluded_colors):
        self.program_time, self.actual_time = program_time, actual_time
        self.tasks.append('REPORT')
        self.label_color = get_random_color(excluded_colors)
        self.messages.append(f'Report {self.running_servers} servers running')

    def create_log(self):
        log = {'program_time':self.program_time, 'event':','.join(self.tasks),
                'message':','.join(self.messages), 'actual_time':self.actual_time,
                'display_message':f'{self.program_time} - {", ".join(self.messages)}'.lower()}
        self.event_log.append(log)

    def get_report(self):
        return self.event_log


    def get_response_data(self, program_time):
        response_message = f'{program_time} - {", ".join(self.messages)}'.lower()
        self.messages.clear()
        self.tasks.clear()
        data = {'message': response_message, 'wall_color': self.wall_color,
                'clock_color': self.clock_color, 'label_color': self.label_color}
        self.create_log()
        return data



    

    