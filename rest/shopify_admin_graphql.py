import httpx
from .shopify_admin_graphql_base import ShopifyAdminGraphQlBase

class ShopifyAdminGraphQl(ShopifyAdminGraphQlBase):
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