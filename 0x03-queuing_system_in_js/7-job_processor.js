import { createQueue } from 'kue';

const blacklist = [
	'4153518780', '4153518781'
];

const queue = createQueue();

/**
 * 
 * @param {String} phoneNumber 
 * @param {String} message 
 * @param {Job} job 
 * @param {*} done 
 */
const sendNotification = (phoneNumber, message, job, done) => {
	let progress = 2, total = 2;

	let sendInterval = setInterval(() => {
		if (total - progress <= total / 2) {
			job.progress(total - progress, total);
		}

		if (blacklist.includes(phoneNumber)) {
			done(new Error(`Phone number ${phoneNumber} is blacklisted`));
			clearInterval(sendInterval);
			return;
		}
		if (total === progress) {
			console.log(
				`Sending notification to ${phoneNumber},`,
				`with message: ${message}`,
			);
		}
		--progress || done();
		progress || clearInterval(sendInterval);
	}, 1000);
}

queue.process('push_notification_code_2', 2, (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});