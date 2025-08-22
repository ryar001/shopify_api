import pytest
import httpx
import asyncio
from unittest.mock import AsyncMock, patch
import os

from rest.shopify_admin_graphql import ShopifyAdminGraphQl
from rest.endpoints import ORDER_CREATE_MUTATION, DRAFT_ORDER_CREATE_MUTATION, ORDER_UPDATE_MUTATION, ORDER_EDIT_BEGIN_MUTATION, DRAFT_ORDER_COMPLETE_MUTATION, DRAFT_ORDER_UPDATE_MUTATION

# --- Unit Tests ---

@pytest.mark.asyncio
async def test_order_create_unit():
    shop_url = "test-shop.myshopify.com"
    access_token = "test_token"
    client = ShopifyAdminGraphQl(shop_url, access_token)

    mock_response_data = {
        "data": {
            "orderCreate": {
                "order": {"id": "gid://shopify/Order/12345", "name": "#1001"},
                "userErrors": []
            }
        }
    }

    with patch.object(client, '_execute_graphql_query', new_callable=AsyncMock) as mock_execute:
        mock_execute.return_value = mock_response_data
        
        input_data = {"lineItems": [{"quantity": 1, "variantId": "gid://shopify/ProductVariant/123"}]}
        response = await client.order_create(input_data)

        mock_execute.assert_called_once_with(
            ORDER_CREATE_MUTATION, {"input": input_data}
        )
        assert response == mock_response_data

@pytest.mark.asyncio
async def test_draft_order_create_unit():
    shop_url = "test-shop.myshopify.com"
    access_token = "test_token"
    client = ShopifyAdminGraphQl(shop_url, access_token)

    mock_response_data = {
        "data": {
            "draftOrderCreate": {
                "draftOrder": {"id": "gid://shopify/DraftOrder/67890", "name": "#D1"},
                "userErrors": []
            }
        }
    }

    with patch.object(client, '_execute_graphql_query', new_callable=AsyncMock) as mock_execute:
        mock_execute.return_value = mock_response_data
        
        input_data = {"lineItems": [{"quantity": 1, "variantId": "gid://shopify/ProductVariant/456"}]}
        response = await client.draft_order_create(input_data)

        mock_execute.assert_called_once_with(
            DRAFT_ORDER_CREATE_MUTATION, {"input": input_data}
        )
        assert response == mock_response_data

# --- Live Tests ---
# To run live tests, set the following environment variables:
# SHOPIFY_SHOP_URL (e.g., your-shop-name.myshopify.com)
# SHOPIFY_ACCESS_TOKEN (e.g., shpat_YOUR_ACCESS_TOKEN)

@pytest.mark.asyncio
@pytest.mark.skipif(
    not os.environ.get("SHOPIFY_SHOP_URL") or not os.environ.get("SHOPIFY_ACCESS_TOKEN"),
    reason="SHOPIFY_SHOP_URL and SHOPIFY_ACCESS_TOKEN environment variables not set"
)
async def test_live_draft_order_create():
    shop_url = os.environ["SHOPIFY_SHOP_URL"]
    access_token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    client = ShopifyAdminGraphQl(shop_url, access_token)

    # Example: Create a simple draft order
    input_data = {
        "lineItems": [
            {
                "quantity": 1,
                "variantId": "gid://shopify/ProductVariant/YOUR_PRODUCT_VARIANT_ID" # REPLACE WITH A REAL PRODUCT VARIANT ID FROM YOUR STORE
            }
        ],
        "customer": {"email": "test@example.com"}
    }

    print(f"\nAttempting to create a draft order on {shop_url}...")
    try:
        response = await client.draft_order_create(input_data)
        print("Live test response:", response)
        assert "data" in response
        assert "draftOrderCreate" in response["data"]
        assert "draftOrder" in response["data"]["draftOrderCreate"]
        assert response["data"]["draftOrderCreate"]["draftOrder"]["id"] is not None
        print(f"Successfully created draft order: {response['data']['draftOrderCreate']['draftOrder']['name']}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP Error during live test: {e.response.status_code} - {e.response.text}")
        pytest.fail(f"Live test failed due to HTTP error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during live test: {e}")
        pytest.fail(f"Live test failed: {e}")

# You can add more live tests for other mutations here.
