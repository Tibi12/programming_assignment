document.addEventListener('DOMContentLoaded', function() {
    // Existing code...
  
    // Function to place order
    placeOrderBtn.onclick = function() {
      var orderItems = Object.entries(order);
      if (orderItems.length > 0) {
        fetch('/api/orders', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(order)
        })
        .then(response => response.json())
        .then(data => {
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
        })
        .catch(error => console.error('Error placing order:', error));
      } else {
        alert('Please add items to your order.');
      }
    };
  
    // Function to fetch ordered items
    fetchOrderedItemsBtn.onclick = function() {
      fetch('/api/orders')
        .then(response => response.json())
        .then(data => {
          orderedItemsDiv.textContent = 'Ordered Items: ' + (data.length > 0 ? data.join(', ') : 'No items ordered.');
        })
        .catch(error => console.error('Error fetching ordered items:', error));
    };
  });
  