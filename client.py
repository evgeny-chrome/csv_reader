import requests
import time

if __name__ == '__main__':
    response = requests.post('http://127.0.0.1:5000/sums/my_data.csv/')
    print(response.status_code)
    print(response.text)
    json_answer = response.json()
    print('Please wait')

    result = 'None'

    while result == 'None':

        time.sleep(0.5)
        response = requests.get('http://127.0.0.1:5000/sums/' + json_answer['task_id'] + '/')
        print()
        print(response.status_code)
        print(response.json())

        result = response.json()['result']
