import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
	console.log('Redis client not connected to the server: ', err.message);
});

client.on('connect', () => {
	console.log('Redis client connected to the server');
});


const createHash = () => {
	let schoolLocations = {
		Portland: 50,
		Seattle: 80,
		'New York': 20,
		Bogota: 20,
		Cali: 40,
		Paris: 2
	}

	for (const [location, students] of Object.entries(schoolLocations)) {
		client.hset("HolbertonSchools", location, students, print)
	}
}

const displayHash = () => {
	client.hgetall("HolbertonSchools", (error, data) =>
		console.log(data)
	)
}

createHash()
displayHash()
