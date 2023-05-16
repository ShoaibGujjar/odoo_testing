import unittest

class TestCreateSalesOrder(unittest.TestCase):

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

    # Create a new sales order in Odoo.
    sales_order = self.env["sale.order"].create({
      "name": "Test Sales Order",
      "customer_id": 1,
      "product_id": 1,
      "quantity": 1,
      "price": 100.00
    })

    # Assert that the sales order was created successfully.
    self.assertEqual(sales_order.id, expected_result["id"])
    self.assertEqual(sales_order.name, expected_result["name"])
    self.assertEqual(sales_order.customer_id, expected_result["customer_id"])
    self.assertEqual(sales_order.product_id, expected_result["product_id"])
    self.assertEqual(sales_order.quantity, expected_result["quantity"])
    self.assertEqual(sales_order.price, expected_result["price"])

if __name__ == "__main__":
  unittest.main()

class TestDeleteSalesOrder(unittest.TestCase):

  def test_delete_sales_order(self):
    """Test that the delete_sales_order function deletes a sales order correctly."""
    # Create a new sales order in Odoo.
    sales_order = self.env["sale.order"].create({
      "name": "Test Sales Order",
      "customer_id": 1,
      "product_id": 1,
      "quantity": 1,
      "price": 100.00
    })

    # Delete the sales order.
    self.env["sale.order"].delete(sales_order.id)

    # Assert that the sales order was deleted successfully.
    with self.assertRaises(Exception):
      self.env["sale.order"].browse(sales_order.id)


class TestUpdateSalesOrder(unittest.TestCase):

  def test_update_sales_order(self):
    """Test that the update_sales_order function updates a sales order correctly."""
    # Create a new sales order in Odoo.
    sales_order = self.env["sale.order"].create({
      "name": "Test Sales Order",
      "customer_id": 1,
      "product_id": 1,
      "quantity": 1,
      "price": 100.00
    })

    # Update the sales order.
    sales_order.write({
      "name": "Updated Test Sales Order",
      "customer_id": 2,
      "product_id": 2,
      "quantity": 2,
      "price": 200.00
    })

    # Assert that the sales order was updated successfully.
    self.assertEqual(sales_order.name, "Updated Test Sales Order")
    self.assertEqual(sales_order.customer_id, 2)
    self.assertEqual(sales_order.product_id, 2)
    self.assertEqual(sales_order.quantity, 2)
    self.assertEqual(sales_order.price, 200.00)

    
if __name__ == "__main__":
  unittest.main()