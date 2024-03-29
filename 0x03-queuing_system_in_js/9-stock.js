import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const listProducts = [
	{
		id: 1,
		name: 'Suitcase 250',
		price: 50,
		stock: 4
	},
	{
		id: 2,
		name: 'Suitcase 450',
		price: 100,
		stock: 10
	},
	{
		id: 3,
		name: 'Suitcase 650',
		price: 350,
		stock: 2
	},
	{
		id: 4,
		name: 'Suitcase 1050',
		price: 550,
		stock: 5
	},
];

const getItemById = (id) => {
	const item = listProducts.find(obj => obj.id === id);

	if (item) {
		return Object.fromEntries(Object.entries(item));
	}
};

const app = express();
const client = createClient();

/**
 * Modifies the reserved stock for a given item.
 * @param {number} id - The id of the item.
 * @param {number} stock - The stock of the item.
 */
const reserveStockById = async (id, stock) => {
	return promisify(client.SET).bind(client)(`item.${id}`, stock);
};

/**
 * Retrieves the reserved stock for a given item.
 * @param {number} id - The id of the item.
 * @returns {Promise<String>}
 */
const getCurrentReservedStockById = async (id) => {
	return promisify(client.GET).bind(client)(`item.${id}`);
};

app.get('/list_products', (_, res) => {
	res.status(200).json(listProducts);
});

app.get('/list_products/:id(\\d+)', (req, res) => {
	const id = Number.parseInt(req.params.id);
	const productItem = getItemById(Number.parseInt(id));

	if (!productItem) {
		res.json({ status: 'Product not found' });
		return;
	}
	getCurrentReservedStockById(id)
		.then((result) => Number.parseInt(result || 0))
		.then((reservedStock) => {
			productItem.currentQuantity = productItem.stock - reservedStock;
			res.json(productItem);
		});
});

app.get('/reserve_product/:id', (req, res) => {
	const id = Number.parseInt(req.params.id);
	const productItem = getItemById(Number.parseInt(id));

	if (!productItem) {
		res.json({ status: 'Product not found' });
		return;
	}
	getCurrentReservedStockById(id)
		.then((result) => Number.parseInt(result || 0))
		.then((reservedStock) => {
			if (reservedStock >= productItem.stock) {
				res.json({ status: 'Not enough stock available', id });
				return;
			}
			reserveStockById(id, reservedStock + 1)
				.then(() => {
					res.json({ status: 'Reservation confirmed', id });
				});
		});
});

const resetProductsStock = () => {
	return Promise.all(
		listProducts.map(
			item => promisify(client.SET).bind(client)(`item.${item.id}`, 0),
		)
	);
};

app.listen(1245, () => {
	resetProductsStock()
		.then(() => {
			console.log(`API available on localhost port ${PORT}`);
		});
});

export default app;