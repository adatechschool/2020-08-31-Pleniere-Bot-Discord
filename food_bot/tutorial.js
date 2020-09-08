const { WebClient } = require('@slack/web-api');

console.log('Getting started with Node Slack SDK');

const web = new WebClient(process.env.SLACK_TOKEN);

const currentTime = new Date().toTimeString();

(async () => {

	try {
		await web.chat.postMessage({
			channel: '#testing',
			text: `Hi ladies, the current time is ${currentTime}`,
		});
	} catch (error) {
		console.log('error');
	}

	console.log('Message posted!');

})();

