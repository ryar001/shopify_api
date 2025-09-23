# GraphQL Mutations for Shopify Orders

ORDER_CREATE_MUTATION = """
mutation orderCreate($input: OrderInput!) {
  orderCreate(input: $input) {
    order {
      id
      name
    }
    userErrors {
      field
      message
    }
  }
}
"""

ORDER_UPDATE_MUTATION = """
mutation orderUpdate($input: OrderInput!) {
  orderUpdate(input: $input) {
    order {
      id
      name
    }
    userErrors {
      field
      message
    }
  }
}
"""

ORDER_EDIT_BEGIN_MUTATION = """
mutation orderEditBegin($id: ID!) {
  orderEditBegin(id: $id) {
    order {
      id
      name
    }
    userErrors {
      field
      message
    }
  }
}
"""

DRAFT_ORDER_CREATE_MUTATION = """
mutation draftOrderCreate($input: DraftOrderInput!) {
  draftOrderCreate(input: $input) {
    draftOrder {
      id
      name
    }
    userErrors {
      field
      message
    }
  }
}
"""

DRAFT_ORDER_COMPLETE_MUTATION = """
mutation draftOrderComplete($id: ID!) {
  draftOrderComplete(id: $id) {
    draftOrder {
      id
      name
    }
    userErrors {
      field
      message
    }
  }
}
"""

DRAFT_ORDER_UPDATE_MUTATION = """
mutation draftOrderUpdate($id: ID!, $input: DraftOrderInput!) {
  draftOrderUpdate(id: $id, input: $input) {
    draftOrder {
      id
      name
    }
    userErrors {
      field
      message
    }
  }
}
"""

ORDER_CREATE_MANUAL_PAYMENT_MUTATION = """
mutation orderCreateManualPayment($id: ID!, $amount: MoneyInput, $paymentMethodName: String, $processedAt: DateTime) {
  orderCreateManualPayment(id: $id, amount: $amount, paymentMethodName: $paymentMethodName, processedAt: $processedAt) {
    order {
      id
    }
    userErrors {
      field
      message
    }
  }
}
"""

SUBSCRIPTION_CONTRACT_CREATE_MUTATION = """
mutation subscriptionContractCreate($input: SubscriptionContractCreateInput!) {
  subscriptionContractCreate(input: $input) {
    draft {
      id
    }
    userErrors {
      field
      message
    }
  }
}
"""

SUBSCRIPTION_BILLING_ATTEMPT_CREATE_MUTATION = """
mutation subscriptionBillingAttemptCreate($subscriptionContractId: ID!, $subscriptionBillingAttemptInput: SubscriptionBillingAttemptInput!) {
  subscriptionBillingAttemptCreate(subscriptionContractId: $subscriptionContractId, subscriptionBillingAttemptInput: $subscriptionBillingAttemptInput) {
    subscriptionBillingAttempt {
      id
      errorMessage
      order {
        id
      }
      ready
    }
    userErrors {
      field
      message
    }
  }
}
"""

GET_PRODUCTS_LISTING_QUERY = """
query GetProductsListing {
  products(first: 10, query: "status:active") {
    nodes {
      id
      title
      handle
      status
    }
  }
}
"""