

from datetime import datetime

# Input datetime string
input_datetime_str = '14 may 2023 22 40'

print(datetime.now())
# Convert to datetime object
input_datetime = datetime.strptime(input_datetime_str, '%d %B %Y %H %M')

# Convert to ISO 8601 format
output_datetime_str = input_datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
end_datetime_str = output_datetime_str
# 2023-05-14T17:10:18.559362Z
# print(output_datetime_str)

if
end_datetime = datetime.fromisoformat(end_datetime_str.replace('Z', '+00:00'))
print(end_datetime)
