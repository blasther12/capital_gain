import json
import sys
import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

from typing import List

from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field

class OperationType(str, Enum):
    BUY = "buy"
    SELL = "sell"

class Operation(BaseModel):
    operation: OperationType
    unit_cost: float = Field(alias="unit-cost")
    quantity: int


class OperationTax(BaseModel):
    tax: float


def calculate_total_cost(avg_price: float, total_quantity: int) -> float:
    """Calculate the current total cost based on average price and quantity."""
    return avg_price * total_quantity


def update_average_price(
    current_total_cost: float,
    unit_cost: float,
    quantity: int,
    total_quantity: int
) -> float:
    """Update the average price after a purchase."""
    
    new_total_cost = current_total_cost + (unit_cost * quantity)
    return new_total_cost / (total_quantity + quantity)


def calculate_profit(
    unit_cost: float,
    quantity: int,
    avg_price: float
) -> float:
    """Calculate the profit from a sell operation."""

    total_sale_value = unit_cost * quantity
    total_cost_value = avg_price * quantity
    return total_sale_value - total_cost_value


def calculate_tax(
    profit: float,
    accumulated_loss: float
) -> List[OperationTax]:
    """Calculate tax based on profit and accumulated loss."""
    adjusted_profit = profit - accumulated_loss
    if adjusted_profit > 0:
        tax = adjusted_profit * 0.2
        return round(tax, 2), 0.0
    else:
        return 0.0, abs(adjusted_profit)


def process_operations(operations: List[Operation]) -> List[OperationTax]:
    """Process a list of operations and calculate taxes."""
    total_quantity = 0
    avg_price = 0.0
    accumulated_loss = 0.0
    results = []

    for operation in operations:
        if operation.operation == "buy":
            current_total_cost = calculate_total_cost(
                avg_price,
                total_quantity
            )
            avg_price = update_average_price(
                current_total_cost,
                operation.unit_cost,
                operation.quantity,
                total_quantity
            )
            total_quantity += operation.quantity
            results.append(OperationTax(tax=0.0))
            continue
        total_sale_value = operation.unit_cost * operation.quantity
        profit = calculate_profit(
            operation.unit_cost,
            operation.quantity,
            avg_price
        )

        if total_sale_value <= 20000:
            if profit < 0:
                accumulated_loss += abs(profit)
            results.append(OperationTax(tax=0.0))
        else:
            tax, accumulated_loss = calculate_tax(profit, accumulated_loss)
            results.append(OperationTax(tax=tax))

        total_quantity -= operation.quantity

    return results

def main():
    input_data = sys.stdin.read()
    for line in input_data.splitlines():
        line = line.strip()
        if not line:
            break
        operations = json.loads(line)
        logging.info(f"Input: {operations}")
        
        operations_validated =  [Operation.model_validate(op) for op in operations]
        impostos = process_operations(operations_validated)
        
        logging.info(f"Output: {[op.model_dump() for op in impostos]}")


if __name__ == "__main__":
    main()
