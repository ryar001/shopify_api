import httpx
import json
from .endpoints import (
    ORDER_CREATE_MUTATION,
    ORDER_UPDATE_MUTATION,
    ORDER_EDIT_BEGIN_MUTATION,
    DRAFT_ORDER_CREATE_MUTATION,
    DRAFT_ORDER_COMPLETE_MUTATION,
    DRAFT_ORDER_UPDATE_MUTATION,
    ORDER_CREATE_MANUAL_PAYMENT_MUTATION,
    SUBSCRIPTION_CONTRACT_CREATE_MUTATION,
    SUBSCRIPTION_BILLING_ATTEMPT_CREATE_MUTATION
)

class ShopifyAdminGraphQl:
    def __init__(self, shop_url: str, access_token: str):
        self.shop_url = shop_url
        self.access_token = access_token
        self.graphql_url = f"https://{self.shop_url}/admin/api/2024-07/graphql.json" # Using a recent API version
        self.headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": self.access_token,
        }

    async def _execute_graphql_query(self, query: str, variables: dict = None):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.graphql_url,
                headers=self.headers,
                json={"query": query, "variables": variables or {}},
            )
            response.raise_for_status()  # Raise an exception for 4xx or 5xx responses
            return response.json()

    async def order_create(self, input: dict):
        """Creates a new order."""
        return await self._execute_graphql_query(ORDER_CREATE_MUTATION, {"input": input})

    async def order_update(self, input: dict):
        """Updates an existing order."""
        return await self._execute_graphql_query(ORDER_UPDATE_MUTATION, {"input": input})

    async def order_edit_begin(self, order_id: str):
        """Begins an order editing session."""
        return await self._execute_graphql_query(ORDER_EDIT_BEGIN_MUTATION, {"id": order_id})

    async def draft_order_create(self, input: dict):
        """Creates a new draft order."""
        return await self._execute_graphql_query(DRAFT_ORDER_CREATE_MUTATION, {"input": input})

    async def draft_order_complete(self, draft_order_id: str):
        """Completes a draft order, turning it into a full order."""
        return await self._execute_graphql_query(DRAFT_ORDER_COMPLETE_MUTATION, {"id": draft_order_id})

    async def draft_order_update(self, draft_order_id: str, input: dict):
        """Updates an existing draft order."""
        return await self._execute_graphql_query(DRAFT_ORDER_UPDATE_MUTATION, {"id": draft_order_id, "input": input})

    async def order_create_manual_payment(self, input: dict):
        """Creates a manual payment for an order."""
        return await self._execute_graphql_query(ORDER_CREATE_MANUAL_PAYMENT_MUTATION, input)
