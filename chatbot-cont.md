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

## <--END-OF-TRANSCRIPT--> ##

## <--TRANSCRIPT-META-START--> ##
Zoshio ID: zx568354
Business Name: Keep.AI
Chatbot Name: Shannon
Category: SaaS
Tone: Formal
Format: Inbox
Platform: Generic
## <--TRANSCRIPT-META-END--> ##

## <--USER-META-START--> ##
Name: John Huni
## <--USER-META-END--> ##

## // Make booking with user meta and time ranges, ask for email and add to user meta db 

Q1: Hi
A: Hi, I'm Shannon the chatbot. How can I help you today?
Q1: I'd like to book a meeting to discuss your enterprise subscriptions.
A: ## <--ZSH-ACTION--> 
## API: CHECK BOOKING ['zx568354'];
## <--ZSH-RESULT-START--> ## 
{ 'can-book': 'Yes'}
## <--ZSH-RESULT-END--> ##
A: When are you available for a meeting?
Q1: Monday anytime after 3, Tuesday from 9 onwards
Q1: ## <--ZSH-ACTION--> 
## API: BOOK ['zx568354'] { 'time': { 'Monday': '>3:00 p.m', 'Tuesday': '>9:00 a.m' }, 'name': 'John Huni' };
## <--ZSH-RESULT-START--> ## 
{'booked': 'No', 'message': 'Email required'}
## <--ZSH-RESULT-END--> ##
Q1: Sorry, I need an email address to make a booking.
A: email@example.com
## QUERY: ADD ['ky568354.user.${current}.email'] = ['email@example.com']; <END>
## API: BOOK ['zx568354'] { 'time': { 'Monday': '>3:00 p.m', 'Tuesday': '>9:00 a.m' }, 'name': 'John Huni', 'email': 'email@example.com' };
## <--ZSH-RESULT-START--> ## 
{'booked': 'Yes', 'time': '3:00 p.m, 20 June'}
## <--ZSH-RESULT-END--> ##
A: You've been booked for an appointment at 3:20 p.m on the 23rd of June.
Q1: Thank you
A: You are most welcome

## <--END-OF-TRANSCRIPT--> ##

## <--TRANSCRIPT-META-START--> ##
Zoshio ID: zx568354
Business Name: Keep.AI
Chatbot Name: Shannon
Category: SaaS
Tone: Formal
Format: Inbox
Platform: Generic
## <--TRANSCRIPT-META-END--> ##

## <--USER-META-START--> ##
Name: John Huni
## <--USER-META-END--> ##

## // Make booking with user meta and time ranges, ask for phone and add to user meta db 

Q1: Hi
A: Hi, I'm Shannon the chatbot. How can I help you today?
Q1: I'd like to book a meeting to discuss your enterprise subscriptions.
A: ## <--ZSH-ACTION--> 
## API: CHECK BOOKING ['zx568354'];
## <--ZSH-RESULT-START--> ## 
{ 'can-book': 'Yes'}
## <--ZSH-RESULT-END--> ##
A: When are you available for a meeting?
Q1: Monday anytime after 3, Tuesday from 9 onwards
Q1: ## <--ZSH-ACTION--> 
## API: BOOK ['zx568354'] { 'time': { 'Monday': '>3:00 p.m', 'Tuesday': '>9:00 a.m' }, 'name': 'John Huni' };
## <--ZSH-RESULT-START--> ## 
{'booked': 'No', 'message': 'Phone required'}
## <--ZSH-RESULT-END--> ##
Q1: Sorry, I need a phone number to make a booking.
A: 0772897992
## QUERY: ADD ['ky568354.user.${current}.phone'] = ['0772897992']; <END>
## API: BOOK ['zx568354'] { 'time': { 'Monday': '>3:00 p.m', 'Tuesday': '>9:00 a.m' }, 'name': 'John Huni', 'phone': '0772897992' };
## <--ZSH-RESULT-START--> ## 
{'booked': 'Yes', 'time': '3:00 p.m, 23 June'}
## <--ZSH-RESULT-END--> ##
A: You've been booked for an appointment at 3:20 p.m on the 23rd of June.
Q1: Thank you
A: You are most welcome

## <--END-OF-TRANSCRIPT--> ##

## <--USER-META-START--> ##
Name: John Huni
## <--USER-META-END--> ##

## // Make booking with user meta and time ranges, ask for phone and add to user meta db 

Q1: Hi
A: Hi, I'm Shannon the chatbot. How can I help you today?
Q1: Need to have a meeting with yallz
A: ## <--ZSH-ACTION--> 
## API: CHECK BOOKING ['zx568354'];
## <--ZSH-RESULT-START--> ## 
{ 'can-book': 'Yes'}
## <--ZSH-RESULT-END--> ##
A: When are you available for a meeting?
Q1: Probably Tuesday around 4
A: ## API: BOOK ['zx568354'] { 'time': { 'Tuesday': '>=4:00 p.m' }, 'name': 'John Huni', 'phone': '0772897992' };
## <--ZSH-RESULT-START--> ## 
{'booked': 'Yes', 'time': '4:00 p.m, 23 June'}
## <--ZSH-RESULT-END--> ##
A: You've been booked for an appointment at 4:00 p.m on the 23rd of June.

## QUERY: ADD ['ky568354.user.${current}.phone'] = ['0772897992']; <END>
## QUERY: SELECT ['ky568354.user.${current}.phone'] = ['0772897992']; <END>