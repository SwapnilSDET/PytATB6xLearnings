response_time_ms = [1200, 1500, 1800]


# def mili_to_sec(x):
#     return x / 1000

# response_time_sec = list(map(mili_to_sec, response_time_ms))

response_time_sec = list(map(lambda x: x / 1000, response_time_ms)) # Using lambda function

print(response_time_sec)