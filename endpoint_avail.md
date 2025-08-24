# Available Endpoints

This document lists all the available methods in the `ShopifyAdminGraphQl` class.

## Methods

### `order_create(self, input: dict)`
Creates a new order.

### `order_update(self, input: dict)`
Updates an existing order.

### `order_edit_begin(self, order_id: str)`
Begins an order editing session.

### `draft_order_create(self, input: dict)`
Creates a new draft order.

### `draft_order_complete(self, draft_order_id: str)`
Completes a draft order, turning it into a full order.

### `draft_order_update(self, draft_order_id: str, input: dict)`
Updates an existing draft order.

### `order_create_manual_payment(self, input: dict)`
Creates a manual payment for an order.
