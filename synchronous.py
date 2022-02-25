import sys
import time
import requests


# Synchronous solution that hits the endpoint 800 times in 2mins
def call_endpoint():
    try:
        response = requests.get("https://q0zjgslzg5.execute-api.us-west-2.amazonaws.com/prod/", timeout=0.1)
        print(response)
    except requests.exceptions.ReadTimeout:
        pass
    except requests.ConnectionError:
        pass
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        raise ValueError('call_endpoint-> Error at Line No: ' + str(exc_tb.tb_lineno) + '-> ' + str(e))


def main():
    try:
        start_time = time.time()
        max_time_diff = 2*60
        count = 0
        while True and int(time.time()) - start_time < max_time_diff:
            call_endpoint()
            count = count + 1

        print(count)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        raise ValueError('main-> Error at Line No: ' + str(exc_tb.tb_lineno) + '-> ' + str(e))


main()
