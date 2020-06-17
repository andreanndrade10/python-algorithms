'''
Function Description:

Complete the timeConversion function in the editor below.
It should return a new string representing the input time in 24 hour format.

s: a string representing time in 12 hour format
Example:

input: 07:05:45PM
output: 19:05:45
'''
def handle_time(twelvehourformat, am_or_pm):
    hour = twelvehourformat.split(':')[0]
    minute = twelvehourformat.split(':')[1]
    second = twelvehourformat.split(':')[2][:2] #exclude the PM or AM 
    if am_or_pm == 'AM':
        print('{}:{}:{}'.format(hour, minute, second))
    else: 
        hour = 12 + int(hour)
        print('{}:{}:{}'.format(str(hour), minute, second))


def timeConversion(twelvehourformat):
    # find() method returns -1 in case it doesn't find it's parameter
    if twelvehourformat.find('AM') == -1:
        handle_time(twelvehourformat,'PM') 
    else:
        handle_time(twelvehourformat, 'AM')
    


if __name__ == "__main__":
    s = input('Choose an hour in 12h format, like hour:minute:second[PM/AM]: ')
    timeConversion(s)