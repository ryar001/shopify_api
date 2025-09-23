
import httpx
import secrets
from urllib.parse import urlencode

from .endpoints import (
    ORDER_CREATE_MUTATION,
    ORDER_UPDATE_MUTATION,
    ORDER_EDIT_BEGIN_MUTATION,
    DRAFT_ORDER_CREATE_MUTATION,
    DRAFT_ORDER_COMPLETE_MUTATION,
    DRAFT_ORDER_UPDATE_MUTATION,
    ORDER_CREATE_MANUAL_PAYMENT_MUTATION,
    SUBSCRIPTION_CONTRACT_CREATE_MUTATION,
    SUBSCRIPTION_BILLING_ATTEMPT_CREATE_MUTATION,
    GET_PRODUCTS_LISTING_QUERY
)

class ShopifyAdminGraphQlOAuth:
    """
    A client for the Shopify Admin GraphQL API that handles the OAuth 2.0 flow.

    This class is designed to be used within a web application framework (e.g., Flask, FastAPI)
    that can manage HTTP redirects and session state.

    Usage Flow:
    1. Instantiate the class with your app's API key, secret, and required scopes.
    2. When a user wants to connect their store, call `get_authorization_url()`.
       - Store the returned `state` in the user's session for security.
       - Redirect the user to the returned `auth_url`.
    3. Shopify will redirect the user back to your specified `redirect_uri`. In that callback handler:
       - Verify that the `state` parameter from Shopify matches the one in the user's session.
       - Get the `code` parameter from the request.
       - Call `request_access_token()` with the `shop_url` and `code`.
    4. The instance is now authenticated and can be used to make API calls.
       The access token can be stored for future use.
    """
    def __init__(self, api_key: str, api_secret_key: str, scopes: list[str]):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.scopes = ",".join(scopes)
        self.access_token = None
        self.shop_url = None
        self.graphql_url = None
        self.headers = None

    def get_authorization_url(self, shop_url: str, redirect_uri: str) -> tuple[str, str]:
        """
        Generates the authorization URL and a state for the OAuth flow.
        The user should be redirected to this URL.
        The state should be stored (e.g., in a session) to verify the callback.
        """
        self.shop_url = shop_url
        state = secrets.token_hex(16)
        params = {
            "client_id": self.api_key,
            "scope": self.scopes,
            "redirect_uri": redirect_uri,
            "state": state,
            "grant_options[]": "per-user",  # Use "per-user" for online access tokens
        }
        auth_url = f"https://{self.shop_url}/admin/oauth/authorize?{urlencode(params)}"
        return auth_url, state

    async def request_access_token(self, shop_url: str, code: str):
        """
        Exchanges the authorization code for an access token.
        This should be called from the callback endpoint after the user authorizes the app.
        """
        self.shop_url = shop_url
        token_url = f"https://{self.shop_url}/admin/oauth/access_token"
        payload = {
            "client_id": self.api_key,
            "client_secret": self.api_secret_key,
            "code": code,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(token_url, json=payload)
            response.raise_for_status()
            data = response.json()
            self.access_token = data["access_token"]
            self._prepare_for_api_calls()
            return self.access_token

    def _prepare_for_api_calls(self):
        """Prepares the instance for making GraphQL API calls after getting a token."""
        if not self.shop_url or not self.access_token:
            raise Exception("Shop URL and access token must be set before making API calls.")
        
        self.graphql_url = f"https://{self.shop_url}/admin/api/2024-07/graphql.json"
        self.headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": self.access_token,
        }

    async def _execute_graphql_query(self, query: str, variables: dict = None):
        if not self.access_token:
            raise Exception("Access token not available. Please complete the OAuth flow first.")
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.graphql_url,
                headers=self.headers,
                json={"query": query, "variables": variables or {}},
            )
            response.raise_for_status()
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

    async def get_products_listing(self):
        """Gets a listing of available products."""
        return await self._execute_graphql_query(GET_PRODUCTS_LISTING_QUERY)
