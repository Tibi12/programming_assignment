var foodItems = [
    { name: 'Pizza', image: 'pizza.jpg' },
    { name: 'Burger', image: 'burger.jpg' },
    { name: 'Fries', image: 'fries.jpg' },
    { name: 'Salad', image: 'salad.jpg' },
    { name: 'Sushi', image: 'sushi.jpg' },
    { name: 'Pasta', image: 'pasta.jpg' },
    { name: 'Sandwich', image: 'sandwich.jpg' },
    { name: 'Steak', image: 'steak.jpg' },
    { name: 'Soup', image: 'soup.jpg' },
    { name: 'Ice Cream', image: 'icecream.jpg' }
  ]; // List of food items
  var order = {}; // Object to store the order with quantities
  
  document.addEventListener('DOMContentLoaded', function() {
    var foodListElement = document.getElementById('foodList');
    var orderListElement = document.getElementById('orderList');
    var placeOrderBtn = document.getElementById('placeOrderBtn');
    var orderStatusElement = document.getElementById('orderStatus');
    var orderedItemsTableBody = document.querySelector('#orderedItemsTable tbody');
    var orderedItemsDiv = document.getElementById('orderedItems');
  
    // Populate food list
    foodItems.forEach(function(item) {
      var foodItemElement = document.createElement('div');
      foodItemElement.classList.add('food-item');
      foodItemElement.innerHTML = `<img src="${item.image}" alt="${item.name}"><br>${item.name}<br><input type="number" class="quantity-selector" value="0" min="0">`;
      foodItemElement.querySelector('.quantity-selector').onchange = function() {
        updateOrder(item.name, parseInt(this.value));
      };
      foodListElement.appendChild(foodItemElement);
    });
  
    // Function to update order with quantity
    function updateOrder(itemName, quantity) {
      if (quantity <= 0) {
        delete order[itemName];
      } else {
        order[itemName] = quantity;
      }
    }
  
    // Function to place order
    placeOrderBtn.onclick = function() {
      var orderItems = Object.entries(order);
      if (orderItems.length > 0) {
        orderStatusElement.textContent = 'Order has been placed!';
        // Clear previous table
        orderedItemsTableBody.innerHTML = '';
        // Add ordered items to table
        orderItems.forEach(function([itemName, quantity]) {
          var row = orderedItemsTableBody.insertRow();
          var cell1 = row.insertCell();
          var cell2 = row.insertCell();
          cell1.textContent = itemName;
          cell2.textContent = quantity;
        });
        order = {};
        updateOrderList();
      } else {
        alert('Please add items to your order.');
      }
    };
  });
  