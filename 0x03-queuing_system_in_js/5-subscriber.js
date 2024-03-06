import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
	console.log('Redis client not connected to the server: ', err.message);
});

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel')

client.on('message', (_error, data) => {
	console.log(data);
	if (data === 'KILL_SERVER') {
		client.unsubscribe();
		client.quit();
	}
})