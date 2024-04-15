const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

let orders = [];

app.get('/api/orders', (req, res) => {
  res.json(orders);
});

app.post('/api/orders', (req, res) => {
  const order = req.body;
  orders.push(order);
  res.status(201).json(order);
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
