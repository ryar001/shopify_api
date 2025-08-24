## On startup
- check the mcp server shopify_api mcp server is up and running, if not, start it with `screen -S shopify_api_mcp -dm npx -y @shopify/dev-mcp@latest`
- always call the learn_shopify_api from shopify_api mcp server to get the latest documentation info from shopify
- 
## Shopify API MCP Tool
- learn_shopify_api: Always call this first when working with Shopify APIs. It provides essential context about supported APIs and generates a conversation ID for tracking usage across tool calls.
- search_docs_chunks: Use when you need to find relevant information across multiple documentation sections or when you don't know the specific path. This tool searches through chunked content which allows for better token matching within smaller content pieces, but may miss some context from individual pages.
- fetch_full_docs: Use when you need complete documentation for a specific API resource and know the exact path (e.g., /docs/api/admin-rest/resources/product). This provides full context without any information loss from chunking.

## when adding new methods in ./rest/shopify_admin_graphql.py
- first call learn_shopify_api to get the latest documentation info from shopify
- then call fetch_full_docs to get the full documentation for the specific API resource
- then implement the method
- then write a unit test for the method
- then write a live test for the method if possible
- add the method and the information to `endpoint_avail.md`
