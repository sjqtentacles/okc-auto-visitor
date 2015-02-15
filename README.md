# okc-auto-visitor

HOW IT WORKS

In the file you'll see a variable at the end named "match." 
The match variable holds the url of a specific query made to Okcupid. What kind of query? 

1] Log onto okcupid
2] click the "Browse Matches" link on the left sidebar

You will see some parameters like "looking for women" or an age range and whatnot. After you fill it out, click "Search" and it will give you a page of results.
The URL of the current page now is what you should put into the match variable, BUT REMEMBER THIS:
At the end of the url there will be a parameter like this "&count=18"
Make sure to change the count to something >=1000, in my example I just did something ridiculous like "=&count=604800"
The reason for this is to load as many results as allowed into the search page (for the python script to find and target/visit). 

The code is set to a 3 second timer to hopefully avoid banning issues (works for me) and you can put as many matches as you'd like as long as you also remember to "findPeople(match)"

Have fun. 
