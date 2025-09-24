from abc import ABC, abstractmethod
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
    GET_PRODUCTS_LISTING_QUERY,
    GET_SUBSCRIPTION_CONTRACTS_QUERY,
    GET_SHOP_INFO_QUERY
)

class ShopifyAdminGraphQlBase(ABC):
    @abstractmethod
    async def _execute_graphql_query(self, query: str, variables: dict = None):
        """Executes a GraphQL query."""
        pass

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

    async def get_subscription_contracts(self):
        """Gets a list of subscription contracts."""
        return await self._execute_graphql_query(GET_SUBSCRIPTION_CONTRACTS_QUERY)

    async def get_shop_info(self):
        """Gets the shop's information."""
        return await self._execute_graphql_query(GET_SHOP_INFO_QUERY)

    async def subscription_contract_create(self, input: dict):
        """Creates a subscription contract."""
        return await self._execute_graphql_query(SUBSCRIPTION_CONTRACT_CREATE_MUTATION, {"input": input})

    async def subscription_billing_attempt_create(self, subscription_contract_id: str, input: dict):
        """Creates a subscription billing attempt."""
        variables = {"subscriptionContractId": subscription_contract_id, "subscriptionBillingAttemptInput": input}
        return await self._execute_graphql_query(SUBSCRIPTION_BILLING_ATTEMPT_CREATE_MUTATION, variables)
