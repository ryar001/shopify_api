# Shopify API Python Client

This project provides a Python client for interacting with the Shopify Admin GraphQL API. It offers two methods for authentication: a direct client using a permanent access token and an OAuth 2.0 client for public applications.

## Project Overview

This repository contains a set of Python scripts to interact with the Shopify Admin GraphQL API. It's designed to be used as a library to build applications that need to communicate with a Shopify store.

The project includes:
- A main application entry point (`main.py`).
- A module for defining GraphQL queries and mutations (`rest/endpoints.py`).
- Two classes for interacting with the Shopify API:
    - `ShopifyAdminGraphQl` for direct authentication.
    - `ShopifyAdminGraphQlOAuth` for OAuth 2.0 authentication.
- A comprehensive test suite using `pytest`.
- Automation scripts for tracking changes and updating the changelog.

## Scripts Description

- **`main.py`**: The main entry point for the application.
- **`rest/endpoints.py`**: Contains all the GraphQL mutations and queries as string constants.
- **`rest/shopify_admin_graphql.py`**: Implements the `ShopifyAdminGraphQl` class, which is a client for the Shopify Admin GraphQL API using a permanent access token.
- **`rest/shopify_admin_graphql_oauth.py`**: Implements the `ShopifyAdminGraphQlOAuth` class, which handles the OAuth 2.0 flow to get an access token before making API calls.
- **`test_shopify_admin_graphql.py`**: Contains unit and live tests for the `ShopifyAdminGraphQl` class.
- **`test_shopify_admin_graphql_oauth.py`**: Contains unit tests for the `ShopifyAdminGraphQlOAuth` class.
- **`automation_scripts/ai-tracker.sh`**: A bash script that automates tracking changes, generating summaries, and committing them.
- **`endpoint_avail.md`**: Lists the available methods in the `ShopifyAdminGraphQl` class.
- **`GEMIINI.md`**: Provides instructions for an AI coding assistant working on this project.
- **`UPDATES.md`**: A changelog that is automatically updated by the `ai-tracker.sh` script.
- **`commands/`**: This directory contains markdown files that define custom commands that can be used with the `gemini` CLI.

## How to Use

### `rest/shopify_admin_graphql.py`

This class provides a simple way to interact with the Shopify Admin GraphQL API using a permanent access token.

**Installation:**

Make sure you have the `httpx` library installed:
```bash
pip install httpx
```

**Usage:**

```python
import asyncio
from rest.shopify_admin_graphql import ShopifyAdminGraphQl

async def main():
    shop_url = "your-shop-name.myshopify.com"
    access_token = "your-admin-api-access-token"

    client = ShopifyAdminGraphQl(shop_url, access_token)

    # Get a list of products
    try:
        products = await client.get_products_listing()
        print(products)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `rest/shopify_admin_graphql_oauth.py`

This class is designed for use in a web application and handles the OAuth 2.0 flow to obtain an access token.

**Installation:**

Make sure you have the `httpx` library installed:
```bash
pip install httpx
```

**Usage:**

The following is a conceptual example of how to use this class in a web framework like Flask or FastAPI.

```python
# In your web application

from rest.shopify_admin_graphql_oauth import ShopifyAdminGraphQlOAuth
import os

# 1. Initialize the client
client = ShopifyAdminGraphQlOAuth(
    api_key=os.environ.get("SHOPIFY_API_KEY"),
    api_secret_key=os.environ.get("SHOPIFY_API_SECRET"),
    scopes=["write_products", "read_products"]
)

# 2. Redirect the user to the authorization URL
# This would be in a route that starts the OAuth flow
def install():
    shop_url = "some-shop.myshopify.com"
    redirect_uri = "https://yourapp.com/callback"
    auth_url, state = client.get_authorization_url(shop_url, redirect_uri)
    # Store the state in the user's session to verify in the callback
    # session['oauth_state'] = state
    # Redirect the user to auth_url
    return redirect(auth_url)

# 3. Handle the callback from Shopify
# This would be in your callback route
async def callback(request):
    # params = request.query_params
    # if session['oauth_state'] != params['state']:
    #     return "Error: state mismatch"

    shop_url = params['shop']
    code = params['code']

    # 4. Request the access token
    access_token = await client.request_access_token(shop_url, code)
    # Store the access token securely for future API calls for this user

    # 5. Make API calls
    products = await client.get_products_listing()
    print(products)
```

## Testing

The project uses `pytest` for testing.

**Running Unit Tests:**

```bash
pytest test_shopify_admin_graphql.py
pytest test_shopify_admin_graphql_oauth.py
```

**Running Live Tests:**

To run the live tests for `test_shopify_admin_graphql.py`, you need to create a `.env` file in the root of the project with your Shopify Admin API access token:

```
SHOPIFY_ADMIN_KEY="shpat_your_access_token"
```

Then, you can run the tests:

```bash
pytest test_shopify_admin_graphql.py
```

**Note:** The live tests for the OAuth flow in `test_shopify_admin_graphql_oauth.py` are not automated as they require user interaction. The file contains instructions on how to test this manually.
