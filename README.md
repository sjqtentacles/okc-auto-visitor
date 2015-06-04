# okc-auto-visitor

<h2>HOW IT WORKS</h2>

In the file you'll see a variable at the end named "match." 
The match variable holds the url of a specific query made to Okcupid. What kind of query? 

<ol>
<li>Log onto okcupid</li>
<li>click the "Browse Matches" link on the left sidebar</li>

<li>You will see some parameters like "looking for women" or an age range and whatnot. After you fill it out, click "Search" and it will give you a page of results.
The URL of the current page now is what you should put into the match variable, BUT REMEMBER THIS:
At the end of the url there will be a parameter like this "&count=18"</li>

<li>Make sure to change the count to something >=1000, in my example I just did something ridiculous like "=&count=604800"
The reason for this is to load as many results as allowed into the search page (for the python script to find and target/visit). </li>

<li>The code is set to a 3 second timer to hopefully avoid banning issues (works for me) and you can put as many matches as you'd like as long as you also remember to "findPeople(match)"</li>

<li>Make sure to put your login credentials in the script at the top (you'll know where).</li>
</ol>

Ah yes and I accidentally left in the mongodb line, which you can expand into web-scraping services or remove if you just want an auto-visitor.
<br/>

Have fun. 
