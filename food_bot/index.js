const { WebClient } = require('@slack/web-api');

console.log('Getting started with Node Slack SDK');

const web = new WebClient(process.env.SLACK_TOKEN);

