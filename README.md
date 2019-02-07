# formatforlicense

The aim of this repository is to resolve the problem of license issues while sharing datasets and labels in token level. We are proposing a representation for sharing dataset among researchers and communities.

For each token, one word from left and one word from right will be given. There is a transmitter and receiver in this process.

Transmitter(which is sharing the tokens) is converting the tokens from folia format to OUR format and is sharing the links of news.

Receiver is getting news from links(In this case, using  justext). Unlabeled Conll files will be created using news and script will try to match tokens of shared format from transmitter with the text of created empty Conll file. If it matches, It will change the label.

Dependencies:

requests
pynlpl
justext


### Convert Folia Files to OUR Format

This script converts all folia files in `source_dir` to our format and saving to `save_dir`

`python3 foliatoconlllike.py source_dir save_dir`

### Getting News with justext

This script gets all news from links in `source_dir` using justext and writes to files in a `save_dir`

`python3 justextnews.py source_dir save_dir`
