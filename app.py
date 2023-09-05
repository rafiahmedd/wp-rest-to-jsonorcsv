from driver import Driver
url = input("Enter the url of the API: ");

options = ['json', 'csv']

userSelectedOption = ''

messageForUser = "Pick an option:\n"

for index, item in enumerate(options):
    messageForUser += f'{index+1}) {item}\n'

messageForUser += 'Your choice: '

while userSelectedOption.lower() not in options:
    userSelectedOption = input(messageForUser)

if url == "":
    ValueError("Error: URL cannot be empty");
else:
    dataProcessor = Driver();
    dataProcessor.startWriting(url, userSelectedOption);