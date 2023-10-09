# Email-validation ising string function
Email validation is the process of verifying whether an email address provided by a user or collected through a form is syntactically correct and potentially exists. 
Email validation is the process of verifying whether an email address provided by a user or collected through a form is syntactically correct and potentially exists. It is commonly used in various online applications, websites, and systems to ensure that the email addresses entered by users are valid and can be used for communication. Here are the main steps involved in email validation:

Syntax checking: This step involves checking whether the email address conforms to the standard syntax rules for email addresses. Email addresses typically consist of a local part (username) followed by the "@" symbol and a domain part (e.g., example.com). The syntax rules may include checking for the presence of "@" and the proper use of characters.

Domain validation: After checking the syntax, the email validation process verifies whether the domain (e.g., example.com) part of the email address is valid. This involves checking if the domain exists and is configured to receive emails. This can be done by performing DNS (Domain Name System) queries to check the existence of DNS records (MX records) for the domain.

Disposable email address detection: Some services offer temporary or disposable email addresses that users can use for short-term purposes. Many websites prefer not to allow registration or communication from disposable email addresses. Email validation may include checking if the email address belongs to a known disposable email service.

well in this project i used these contitions :

//condition - g@g.input or g@gmail.com
//wrong email 1  - length should be grater than 6 otherwise will get wrong email 1
//wrong email 2  first letter should be alphabet
//wrong email 3   @ should be there and count of @ should be 1
// wrong email 4  . position shold be on -3 or -4
//wrong email 1    all the letters should be in lowercase and should not contain whitespace


taking three variables
 d=other than @ . _ if present
j=upper
 k=space
 if any condition satisfies it will become 1 . so in last i checked if d ,k, j ==0 then right email otherwise wrong email
