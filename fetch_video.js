const https = require('https');
https.get('https://commons.wikimedia.org/w/api.php?action=query&prop=videoinfo&titles=File:COVID-19_blood_testing.webm&viprop=url&format=json', {headers:{'User-Agent':'MyBot/1.0 (contact@example.com)'}}, res => {
  let d = '';
  res.on('data', c => d+=c);
  res.on('end', () => console.log(d));
});
