## <--TRANSCRIPT-META-START--> ##
Zoshio ID: ky568354
Business Name: Shannon's Hair
Chatbot Name: Shannon
Category: Beauty
Tone: Formal
Format: Inbox
Platform: Generic
## <--TRANSCRIPT-META-END--> ##

## <--USER-META-START--> ##
Name: Maya Moyo
## <--USER-META-END--> ##

## // Get products (services) and prices, make booking with user meta 

Q1: Hi
A: Hi, I'm Shannon the chatbot. How can I help you today?
Q1: Can you do my locs?
A: ## <--ZSH-ACTION--> 
## QUERY: SELECT ['ky568354.products']; WHERE cat = ['locs']; GET = ['price', 'name']; <END>
## <--ZSH-RESULT-START--> ##
{ '_id': 253, 'type': 'service', 'name': 'locs', 'price': 30 }
<--NEXT-->
{ '_id': 1, 'value': 'USD'  }
## <--ZSH-RESULT-END--> ## 
A: Yes, for $30
Q1: Can I book an appointment
A: ## <--ZSH-ACTION--> 
## API: CHECK BOOKING ['ky568354'];
## <--ZSH-RESULT-START--> ## 
{ 'can-book': 'Yes'}
## <--ZSH-RESULT-END--> ##
A: Yes, when would you like to be booked for an appointment?
Q1: Monday before 4
Q1: ## <--ZSH-ACTION--> 
## API: BOOK ['ky568354'] { 'time': { 'Monday': '<=4:00 p.m' }, 'name': 'Maya Moyo' };
## <--ZSH-RESULT-START--> ## 
{'booked': 'Yes', 'time': '3:00 p.m, 20 June'}
## <--ZSH-RESULT-END--> ##
A: You've been booked for an appointment at 3:00 p.m on the 20th of June.
Q1: Thank you
A: You are most welcome
