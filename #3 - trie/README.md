# trie

Auto-complete in Google is pretty cool, but implementing it is even more fun!

We use a basic Data Structure called _trie_ for it. 

Here's a very good [article](https://www.geeksforgeeks.org/trie-insert-and-search/) on it. Every trie has an insert 
and search function. We do insertion to save our elements, and then the search makes sure we can find them based 
on the available matches.

I have done an implementation of trie where I save user's and their phone numbers.
The search feature finds the first name based on the digits your enter. 

`add_number` and `dial` are the functions you would want to look at.
