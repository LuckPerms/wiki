# indexer

Uses [mistune](https://github.com/lepture/mistune) (Python) and [lunr](https://lunrjs.com/) (NodeJS) to generate an index for the wiki content.

### Setup
You'll need `node`, `npm`, `python3` and `pip3` available.

```bash
npm install
pip3 install -r requirements.txt
```

### Usage
Generating plaintext output:

```bash
python3 gen_plain.py ../pages/ > plain.json
```

Creating the index
```bash
cat plain.json | node gen_index.js > index.json
```