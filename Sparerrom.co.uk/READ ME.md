READ ME

Objective:
The aim of this script is to give the user a helping hand for searching for flats in London. As the rental market becomes more competitive with each passing day software developers need all the help they can get!

The script searchs Sparroom.co.uk and scans for listings (within a select time frame) that have been put onto the market. As soon as a new listing is available, the script will send the user an email letting them know the details. This means the user will know staright away and can be the first to arrange a viewing. Talk about getting your foot in the door!

How the script works:

Using Selenium Webdriver, the sript autonomosly opens an insantce of Spareroom.co.uk. It will then input paramteres defined by the user (such as postcode, minimum and maximum rent values), it will then scan each lisiting and check if its been seen before (WARNING!! THIS SCRIPT IS RELYING ON THE USER TO HAVE SEARCHED BEFORE, THEREFORE ON ITS FIRST ITTERATION IT WILL NOT SEND ANY EMAILS ABOUT LISTINGS ALREADY ON THE WEBSITE!!).
If the listing is new, the user will get an email with the title of the listing, text summarising listing details and rent prices. SIMPLE!




