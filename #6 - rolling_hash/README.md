# rolling_hash

Well, it sounds good but the idea is even better. Ever wondered how we can find a sub-string within a string
in O(n) time? 

With a rolling hash, we give our `needle` a hash and then try finding it in a `haystack`. 
If a string with the same length of our `needle` matches the length of the substring in the `haystack` then we
return a `True`, else we remove the hashed character from the beginning and add a new one at the end to 
try again. Have a look at the code and feel free to reach out if you think I should elaborate further. 