import { createClient, print } from 'redis';
import { promisify } from 'util'

const client = createClient();

client.on('error', (err) => {
	console.log('Redis client not connected to the server: ', err.message);
});

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

/**
 * Sets a new school
 * @param {String} schoolName - Key: Name of the school
 * @param {String} value - Value for name of the school
 * 
 * @returns {void} Displays a confirmation message
 */
const setNewSchool = (schoolName, value) => {
	client.SET(schoolName, value, print)
}

/**
 * Displays the value for the key passed as argument
 * @param {String} schoolName - Key: Name of the school
 * 
 * @returns {void} Logs to the console the value for the key passed as argument
 */
const displaySchoolValue = async (schoolName) => {
	console.log(await promisify(client.GET).bind(client)(schoolName))
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');