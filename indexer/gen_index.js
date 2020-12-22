const lunr = require('lunr');
const stdin = process.stdin;
const stdout = process.stdout;
const buffer = [];

stdin.resume();
stdin.setEncoding('utf8');

stdin.on('data', (data) => {
  buffer.push(data)
});

stdin.on('end', () => {
  const data = JSON.parse(buffer.join(''))
  const index = lunr(function() {
    this.ref('id');
    this.field('body');
    this.metadataWhitelist = ['position']

    for (const [id, body] of Object.entries(data)) {
      this.add({ id: id, body: body });
    }
  });
  stdout.write(JSON.stringify(index));
});
