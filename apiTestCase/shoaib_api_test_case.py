import requests
import unittest
from configuration import saleOrder

def test_create_sales_order(self):
  """Test that the create_sales_order function creates a new sales order correctly."""
  expected_result = {
    "id": 1,
    "name": "Test Sales Order",
    "customer_id": 1,
    "product_id": 1,
    "quantity": 1,
    "price": 100.00
  }

  # Make a request to the Odoo API to create a new sales order.
  response = requests.post(
    saleOrder,
    json={
      "name": "Test Sales Order",
      "customer_id": 1,
      "product_id": 1,
      "quantity": 1,
      "price": 100.00
    }
  )

  # Assert that the response is successful.
  self.assertEqual(response.status_code, 201)

  # Assert that the response body contains the expected sales order data.
  actual_result = response.json()
  self.assertEqual(actual_result, expected_result)



def test_delete_sales_order(self):
  """Test that the delete_sales_order function deletes a sales order correctly."""
  # Create a new sales order in Odoo.
  response = requests.post(
    saleOrder,
    json={
      "name": "Test Sales Order",
      "customer_id": 1,
      "product_id": 1,
      "quantity": 1,
      "price": 100.00
    }
  )

  # Assert that the response is successful.
  self.assertEqual(response.status_code, 201)

  # Get the sales order ID.
  sales_order_id = response.json()["id"]

  # Delete the sales order.
  response = requests.delete(
    f'{saleOrder}/{sales_order_id}'
  )

  # Assert that the response is successful.
  self.assertEqual(response.status_code, 204)

  # Assert that the sales order was deleted successfully.
  with self.assertRaises(Exception):
    response = requests.get(f"{saleOrder}/{sales_order_id}")



def test_update_sales_order(self):
  """Test that the update_sales_order function updates a sales order correctly."""
  # Create a new sales order in Odoo.
  response = requests.post(
    saleOrder,
    json={
      "name": "Test Sales Order",
      "customer_id": 1,
      "product_id": 1,
      "quantity": 1,
      "price": 100.00
    }
  )

  # Assert that the response is successful.
  self.assertEqual(response.status_code, 201)

  # Get the sales order ID.
  sales_order_id = response.json()["id"]

  # Update the sales order.
  response = requests.put(
    f"{saleOrder}/{sales_order_id}",
    json={
      "name": "Updated Test Sales Order",
      "customer_id": 2,
      "product_id": 2,
      "quantity": 2,
      "price": 200.00
    }
  )

  # Assert that the response is successful.
  self.assertEqual(response.status_code, 200)

  # Get the updated sales order.
  updated_sales_order = requests.get(f"{saleOrder}/{sales_order_id}").json()

  # Assert that the sales order was updated successfully.
  self.assertEqual(updated_sales_order["name"], "Updated Test Sales Order")
  self.assertEqual(updated_sales_order["customer_id"], 2)
  self.assertEqual(updated_sales_order["product_id"], 2)
  self.assertEqual(updated_sales_order["quantity"], 2)
  self.assertEqual(updated_sales_order["price"], 200.00)

if __name__ == "__main__":
  unittest.main()

