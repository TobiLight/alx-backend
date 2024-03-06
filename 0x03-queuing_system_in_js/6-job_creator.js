import { createQueue } from 'kue';

const dataObj = {
	phoneNumber: '2349057737872',
	message: "I will find you!",
}

const queue = createQueue({ name: 'push_notification_code' });

const queueName = "push_notification_code";

const job = queue.create(queueName, dataObj)

job
	.on('enqueue', () => {
		console.log('Notification job created:', job.id);
	})
	.on('complete', () => {
		console.log('Notification job completed');
	})
	.on('failed attempt', () => {
		console.log('Notification job failed');
	});

job.save()