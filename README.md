# formatforlicense

The aim of this repository is to resolve the problem of license issues while sharing datasets and labels in token level. We are proposing a representation for sharing dataset among researchers and communities.

For each token, one word from left and one word from right will be given. There is a transmitter and receiver in this process.

Transmitter(which is sharing the tokens) is converting the tokens from folia format to OUR format and is sharing the links of news.

Receiver is getting news from links(In this case, using  justext), using these news unlabeled Conll files will be created and will try to match tokens of shared format from transmitter with the text of created empty Conll file. If matches, It will change the label.
