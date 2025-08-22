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
