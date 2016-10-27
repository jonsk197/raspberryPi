#AnswerToQuestions
1. Why do we validate data before sending it to the server at client­side, as opposed to just letting
the server validate data before using it? What we get and what we lose by it?

One aspect of it is that we want to minimizing the load on the server and there for not send requests that we know will be denied. If not all the fields in the signup form is filled in we dont have to send it to the server to validate this. But the client side validation is easy to bypass so we need to do some checks at the server, mostly checks concerning security is performed at the server.

2. How secure is the system using an access token to authenticate? Is there any way to circumvent
it and get access to private data?

By saving the token at the user it is fairly easy to steal it  for a hacker/ attacker and to authenticate as the user. Then the attacker have the users acces rights and the same possibility to check for the users private data as the user would have.

3. What would happen if a user were to post a message containing JavaScript­code? Would the
code be executed? How can it oppose a threat to the system? What would the counter measure?

By injecting javascript into the html code the attacker can get the code running on the site. This is bad because the attacker can come across usernames and passwords for example, or get access to the users token. By escape <, >,& and more HTML/ javascript specific signs you can cause the code to be handled as just chars instead of html/ javascript. 


4. What happens when we use the back/forward buttons while working with Twidder ? Is this the
expected behaviour? Why are we getting this behaviour? What would be the solution?

The buttons are not even clickable. This because the page is designed as a single page application, there is not page to move between. We only have on html-file. We could use the HTML5 history API to manipulate the browser history by calling methods like history.pushState() to manually add something to the history.


5. What happens when the user refreshes the page while working with Twidder ? Is this the
expected behaviour? Why are we getting this behaviour?

It returns to the default tab if the view was profileview. If the welcomeview was selected it stays there.

6. Is it a good idea to read views from the server instead of embedding them inside of the
“client.html”? What are the advantages and disadvantages of it comparing to the current
approach?

This is not good because if we have more than a couple of users because the server will be flooded with traffic.

7. Is it a good idea to return true or false to state if an operation has gone wrong at the server­side
or not? How can it be improved?

This is not good because a person trying to find a loophole in the software gets a true or false answer when he sending malformed requests to the server.

8. Is it reliable to perform data validation at client­side? If so please explain how and if not what
would be the solution to improve it?


9. Why isn’t it a good idea to use tablesfor layout purposes? What would be the replacement?

Tables are used for displaying data and should not be used for layout purposes. We should seperate the design code from the data code. The design code should be done in CSS and the data code should be done in HTML. Its better to use div:s for this.


10. How do you think Single Page Applications can contribute to the future of the web? What is
their advantages and disadvantages from usage and development point of views?

